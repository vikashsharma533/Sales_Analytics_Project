from pathlib import Path
import pandas as pd

# Read sales dataset
base_path = Path(__file__).resolve().parent.parent
file_path = base_path / "data" / "raw" / "superstore.csv"

df = pd.read_csv(file_path)

print("Sales Data Validation")
print("-" * 30)

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nFirst 5 Records:")
print(df.head())