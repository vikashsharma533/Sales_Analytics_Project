from pathlib import Path
import pandas as pd
import pyodbc

# Project paths
project_path = Path(__file__).resolve().parent.parent
data_file = project_path / "data" / "cleaned" / "superstore_cleaned.csv"

# SQL Server connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"          # Change if your SQL instance is different
    "DATABASE=SalesAnalyticsDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Load cleaned dataset
df = pd.read_csv(data_file)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])

print(f"Loaded {len(df)} records")

#  Customers 

print("Loading Customers...")

customers = df[["CustomerID", "CustomerName", "Segment"]].drop_duplicates()

for _, row in customers.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Customers
            WHERE CustomerID = ?
        )
        INSERT INTO Customers (CustomerID, CustomerName, Segment)
        VALUES (?, ?, ?)
    """,
    row.CustomerID,
    row.CustomerID,
    row.CustomerName,
    row.Segment)

conn.commit()

# Products 

print("Loading Products...")

products = df[
    ["ProductID", "ProductName", "Category", "SubCategory"]
].drop_duplicates()

for _, row in products.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Products
            WHERE ProductID = ?
        )
        INSERT INTO Products (ProductID, ProductName, Category, SubCategory)
        VALUES (?, ?, ?, ?)
    """,
    row.ProductID,
    row.ProductID,
    row.ProductName,
    row.Category,
    row.SubCategory)

conn.commit()

# Orders 

print("Loading Orders...")

orders = df[
    ["OrderID", "OrderDate", "ShipDate", "ShipMode", "OrderPriority"]
].drop_duplicates()

for _, row in orders.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Orders
            WHERE OrderID = ?
        )
        INSERT INTO Orders
        (OrderID, OrderDate, ShipDate, ShipMode, OrderPriority)
        VALUES (?, ?, ?, ?, ?)
    """,
    row.OrderID,
    row.OrderID,
    row.OrderDate,
    row.ShipDate,
    row.ShipMode,
    row.OrderPriority)

conn.commit()

#  Locations

print("Loading Locations...")

locations = df[
    ["Country", "Market", "Region", "State", "City"]
].drop_duplicates()

for _, row in locations.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Locations
            WHERE Country = ?
              AND Market = ?
              AND Region = ?
              AND State = ?
              AND City = ?
        )
        INSERT INTO Locations
        (Country, Market, Region, State, City)
        VALUES (?, ?, ?, ?, ?)
    """,
    row.Country,
    row.Market,
    row.Region,
    row.State,
    row.City,
    row.Country,
    row.Market,
    row.Region,
    row.State,
    row.City)

conn.commit()

print("Creating Location Mapping...")

cursor.execute("""
SELECT
    LocationID,
    Country,
    Market,
    Region,
    State,
    City
FROM Locations
""")

location_map = {}

for row in cursor.fetchall():
    location_map[
        (
            row.Country,
            row.Market,
            row.Region,
            row.State,
            row.City
        )
    ] = row.LocationID

# Sales

print("Loading Sales...")

for _, row in df.iterrows():

    location_id = location_map[
        (
            row.Country,
            row.Market,
            row.Region,
            row.State,
            row.City
        )
    ]

    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Sales
            WHERE RowID = ?
        )
        INSERT INTO Sales
        (
            RowID,
            OrderID,
            CustomerID,
            ProductID,
            LocationID,
            Sales,
            Quantity,
            Discount,
            Profit,
            ShippingCost,
            SalesYear,
            WeekNum
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    row.RowID,
    row.RowID,
    row.OrderID,
    row.CustomerID,
    row.ProductID,
    location_id,
    row.Sales,
    row.Quantity,
    row.Discount,
    row.Profit,
    row.ShippingCost,
    row.Year,
    row.weeknum)

conn.commit()

print("\nData loaded successfully.")

conn.close()