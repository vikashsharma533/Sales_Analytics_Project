from pathlib import Path
import pandas as pd

# ===========================
# Project Paths
# ===========================

project_root = Path(__file__).resolve().parent.parent

raw_file = project_root / "data" / "raw" / "superstore.csv"
cleaned_file = project_root / "data" / "cleaned" / "superstore_cleaned.csv"

# ===========================
# Load Dataset
# ===========================

df = pd.read_csv(raw_file)

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

print(f"Original Shape : {df.shape}")

# ===========================
# Remove Unnecessary Column
# ===========================

if "记录数" in df.columns:
    df.drop(columns=["记录数"], inplace=True)
    print("✓ Removed column : 记录数")

# ===========================
# Rename Columns
# ===========================

df.rename(columns={
    "Order.ID": "OrderID",
    "Order.Date": "OrderDate",
    "Ship.Date": "ShipDate",
    "Ship.Mode": "ShipMode",
    "Customer.ID": "CustomerID",
    "Customer.Name": "CustomerName",
    "Product.ID": "ProductID",
    "Product.Name": "ProductName",
    "Sub.Category": "SubCategory",
    "Order.Priority": "OrderPriority",
    "Shipping.Cost": "ShippingCost",
    "Row.ID": "RowID"
}, inplace=True)

# ===========================
# Convert Dates
# ===========================

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])

# ===========================
# Final Checks
# ===========================

print(f"Final Shape : {df.shape}")
print("\nMissing Values")
print(df.isnull().sum())

# ===========================
# Save Clean Dataset
# ===========================

df.to_csv(cleaned_file, index=False)

print("\n✅ Cleaned dataset saved successfully.")
print(f"Location : {cleaned_file}")