import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=SalesAnalyticsDB;"
    "Trusted_Connection=yes;"
)

print("✅ Connected Successfully!")

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM Customers")
print("Customers table exists. Rows:", cursor.fetchone()[0])

conn.close()