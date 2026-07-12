from pathlib import Path
import pandas as pd

# ==========================
# Paths
# ==========================

project_root = Path(__file__).resolve().parent.parent

file = project_root / "data" / "cleaned" / "superstore_cleaned.csv"

df = pd.read_csv(file)

print("=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

print("\nMemory Usage")
print(df.memory_usage(deep=True).sum()/1024/1024,"MB")