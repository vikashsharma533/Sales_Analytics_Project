USE SalesAnalyticsDB;
GO

/*
1. Total Sales
*/
SELECT
    SUM(Sales) AS TotalSales
FROM Sales;
GO

/*
2. Total Profit
*/
SELECT
    SUM(Profit) AS TotalProfit
FROM Sales;
GO

/*
3. Total Orders
*/
SELECT
    COUNT(DISTINCT OrderID) AS TotalOrders
FROM Sales;
GO

/*
4. Top 10 Products by Sales
*/
SELECT TOP 10
    p.ProductName,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSales DESC;
GO

/*
5. Top 10 Customers by Sales
*/
SELECT TOP 10
    c.CustomerName,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c
ON s.CustomerID = c.CustomerID
GROUP BY c.CustomerName
ORDER BY TotalSales DESC;
GO

/*
6. Category Wise Sales
*/
SELECT
    p.Category,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalSales DESC;
GO

/*
7. Region Wise Sales
*/
SELECT
    l.Region,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Locations l
ON s.LocationID = l.LocationID
GROUP BY l.Region
ORDER BY TotalSales DESC;
GO

/*
8. Monthly Sales Trend
*/
SELECT
    o.OrderDate,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Orders o
ON s.OrderID = o.OrderID
GROUP BY o.OrderDate
ORDER BY o.OrderDate;
GO

/*
9. Top 10 Profitable Products
*/
SELECT TOP 10
    p.ProductName,
    SUM(s.Profit) AS TotalProfit
FROM Sales s
JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalProfit DESC;
GO

/*
10. Average Discount
*/
SELECT
    AVG(Discount) AS AverageDiscount
FROM Sales;
GO