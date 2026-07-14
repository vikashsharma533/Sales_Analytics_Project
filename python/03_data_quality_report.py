from pathlib import Path
import pandas as pd

# Read cleaned dataset
project_path = Path(__file__).resolve().parent.parent
data_file = project_path / "data" / "cleaned" / "superstore_cleaned.csv"

df = pd.read_csv(data_file)

print("Data Quality Report")
print("-" * 30)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

print("\nMemory Usage")
print(f"{memory:.2f} MB")