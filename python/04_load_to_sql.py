import pandas as pd
import pyodbc

# -----------------------------
# SQL Server Connection
# -----------------------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=SalesAnalyticsDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# -----------------------------
# Read Cleaned CSV
# -----------------------------
df = pd.read_csv("data/cleaned/superstore_cleaned.csv")

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])

print(f"Loaded {len(df)} rows")

# -----------------------------
# Customers
# -----------------------------
print("Loading Customers...")

customers = df[["CustomerID", "CustomerName", "Segment"]].drop_duplicates()

for _, row in customers.iterrows():
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1 FROM Customers WHERE CustomerID=?
        )
        INSERT INTO Customers(CustomerID,CustomerName,Segment)
        VALUES(?,?,?)
    """,
    row.CustomerID,
    row.CustomerID,
    row.CustomerName,
    row.Segment)

conn.commit()

# -----------------------------
# Products
# -----------------------------
print("Loading Products...")

products = df[
    ["ProductID","ProductName","Category","SubCategory"]
].drop_duplicates()

for _, row in products.iterrows():
    cursor.execute("""
        IF NOT EXISTS(
            SELECT 1 FROM Products WHERE ProductID=?
        )
        INSERT INTO Products
        VALUES(?,?,?,?)
    """,
    row.ProductID,
    row.ProductID,
    row.ProductName,
    row.Category,
    row.SubCategory)

conn.commit()

# -----------------------------
# Orders
# -----------------------------
print("Loading Orders...")

orders = df[
    ["OrderID","OrderDate","ShipDate","ShipMode","OrderPriority"]
].drop_duplicates()

for _, row in orders.iterrows():
    cursor.execute("""
        IF NOT EXISTS(
            SELECT 1 FROM Orders WHERE OrderID=?
        )
        INSERT INTO Orders
        VALUES(?,?,?,?,?)
    """,
    row.OrderID,
    row.OrderID,
    row.OrderDate,
    row.ShipDate,
    row.ShipMode,
    row.OrderPriority)

conn.commit()

# -----------------------------
# Locations
# -----------------------------
print("Loading Locations...")

locations = df[
    ["Country","Market","Region","State","City"]
].drop_duplicates()

for _, row in locations.iterrows():

    cursor.execute("""
        IF NOT EXISTS(
            SELECT 1
            FROM Locations
            WHERE Country=?
            AND Market=?
            AND Region=?
            AND State=?
            AND City=?
        )
        INSERT INTO Locations
        VALUES(?,?,?,?,?)
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

print("Building Location Mapping...")

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

for r in cursor.fetchall():
    location_map[
        (
            r.Country,
            r.Market,
            r.Region,
            r.State,
            r.City
        )
    ] = r.LocationID

# -----------------------------
# Sales
# -----------------------------
print("Loading Sales...")

for _, row in df.iterrows():

    locid = location_map[
        (
            row.Country,
            row.Market,
            row.Region,
            row.State,
            row.City
        )
    ]

    cursor.execute("""
    IF NOT EXISTS(
        SELECT 1 FROM Sales WHERE RowID=?
    )
    INSERT INTO Sales
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    row.RowID,
    row.RowID,
    row.OrderID,
    row.CustomerID,
    row.ProductID,
    locid,
    row.Sales,
    row.Quantity,
    row.Discount,
    row.Profit,
    row.ShippingCost,
    row.Year,
    row.weeknum)

conn.commit()

print("=================================")
print("DATA LOADED SUCCESSFULLY")
print("=================================")

conn.close()