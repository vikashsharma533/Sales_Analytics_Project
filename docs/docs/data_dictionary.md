# Data Dictionary

This document describes the database tables and columns used in the Sales Analytics project.

---

# Customers

| Column | Data Type | Description |
|--------|-----------|-------------|
| CustomerID | NVARCHAR(30) | Unique customer identifier |
| CustomerName | NVARCHAR(150) | Customer name |
| Segment | NVARCHAR(50) | Customer segment |

---

# Products

| Column | Data Type | Description |
|--------|-----------|-------------|
| ProductID | NVARCHAR(50) | Unique product identifier |
| ProductName | NVARCHAR(300) | Product name |
| Category | NVARCHAR(100) | Product category |
| SubCategory | NVARCHAR(100) | Product sub-category |

---

# Orders

| Column | Data Type | Description |
|--------|-----------|-------------|
| OrderID | NVARCHAR(30) | Unique order identifier |
| OrderDate | DATE | Order date |
| ShipDate | DATE | Shipping date |
| ShipMode | NVARCHAR(50) | Shipping method |
| OrderPriority | NVARCHAR(30) | Order priority |

---

# Locations

| Column | Data Type | Description |
|--------|-----------|-------------|
| LocationID | INT | Unique location identifier |
| Country | NVARCHAR(100) | Country |
| Market | NVARCHAR(100) | Sales market |
| Region | NVARCHAR(100) | Region |
| State | NVARCHAR(100) | State |
| City | NVARCHAR(100) | City |

---

# Sales

| Column | Data Type | Description |
|--------|-----------|-------------|
| RowID | INT | Unique transaction identifier |
| OrderID | NVARCHAR(30) | Reference to Orders table |
| CustomerID | NVARCHAR(30) | Reference to Customers table |
| ProductID | NVARCHAR(50) | Reference to Products table |
| LocationID | INT | Reference to Locations table |
| Sales | DECIMAL(18,2) | Sales amount |
| Quantity | INT | Quantity sold |
| Discount | DECIMAL(10,2) | Discount percentage |
| Profit | DECIMAL(18,2) | Profit amount |
| ShippingCost | DECIMAL(18,2) | Shipping cost |
| SalesYear | INT | Sales year |
| WeekNum | INT | Week number |