from pathlib import Path
import pandas as pd

# Project Root
project_root = Path(__file__).resolve().parent.parent

# Dataset Path
csv_path = project_root / "data" / "raw" / "superstore.csv"

# Read Dataset
df = pd.read_csv(csv_path)

print("=" * 50)
print("SALES DATA VALIDATION")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())