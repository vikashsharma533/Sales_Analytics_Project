USE SalesAnalyticsDB;
GO

-- Total Sales

SELECT SUM(Sales) AS TotalSales
FROM Sales;
GO


-- Total Profit

SELECT SUM(Profit) AS TotalProfit
FROM Sales;
GO


-- Total Orders

SELECT COUNT(DISTINCT OrderID) AS TotalOrders
FROM Sales;
GO


-- Total Customers

SELECT COUNT(DISTINCT CustomerID) AS TotalCustomers
FROM Sales;
GO


-- Total Products

SELECT COUNT(DISTINCT ProductID) AS TotalProducts
FROM Sales;
GO


-- Category Wise Sales

SELECT
    p.Category,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalSales DESC;
GO


-- Market Wise Sales

SELECT
    l.Market,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Locations l
ON s.LocationID = l.LocationID
GROUP BY l.Market
ORDER BY TotalSales DESC;
GO


-- Region Wise Sales

SELECT
    l.Region,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Locations l
ON s.LocationID = l.LocationID
GROUP BY l.Region
ORDER BY TotalSales DESC;
GO


-- Top 10 Countries

SELECT TOP 10
    l.Country,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Locations l
ON s.LocationID = l.LocationID
GROUP BY l.Country
ORDER BY TotalSales DESC;
GO


-- Sales by Year

SELECT
    SalesYear,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM Sales
GROUP BY SalesYear
ORDER BY SalesYear;
GO


-- Monthly Sales

SELECT
    YEAR(o.OrderDate) AS SalesYear,
    MONTH(o.OrderDate) AS SalesMonth,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Orders o
ON s.OrderID = o.OrderID
GROUP BY
    YEAR(o.OrderDate),
    MONTH(o.OrderDate)
ORDER BY
    SalesYear,
    SalesMonth;
GO


-- Top Customers

SELECT TOP 10
    c.CustomerName,
    SUM(s.Sales) AS TotalSales,
    SUM(s.Profit) AS TotalProfit
FROM Sales s
INNER JOIN Customers c
ON s.CustomerID = c.CustomerID
GROUP BY c.CustomerName
ORDER BY TotalSales DESC;
GO


-- Segment Analysis

SELECT
    c.Segment,
    SUM(s.Sales) AS TotalSales,
    SUM(s.Profit) AS TotalProfit
FROM Sales s
INNER JOIN Customers c
ON s.CustomerID = c.CustomerID
GROUP BY c.Segment
ORDER BY TotalSales DESC;
GO


-- Best Selling Products

SELECT TOP 10
    p.ProductName,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSales DESC;
GO


-- Lowest Selling Products

SELECT TOP 10
    p.ProductName,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSales;
GO


-- Most Profitable Products

SELECT TOP 10
    p.ProductName,
    SUM(s.Profit) AS TotalProfit
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalProfit DESC;
GO


-- Profit Margin

SELECT
    p.Category,
    SUM(s.Sales) AS TotalSales,
    SUM(s.Profit) AS TotalProfit,
    ROUND((SUM(s.Profit) * 100.0) / SUM(s.Sales),2) AS ProfitMargin
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.Category;
GO


-- Average Order Value

SELECT
    AVG(OrderValue) AS AverageOrderValue
FROM
(
    SELECT
        OrderID,
        SUM(Sales) AS OrderValue
    FROM Sales
    GROUP BY OrderID
) AS OrdersData;
GO


-- Top Cities

SELECT TOP 10
    l.City,
    SUM(s.Sales) AS TotalSales
FROM Sales s
INNER JOIN Locations l
ON s.LocationID = l.LocationID
GROUP BY l.City
ORDER BY TotalSales DESC;
GO


-- Product Ranking

SELECT
    p.ProductName,
    SUM(s.Sales) AS TotalSales,
    DENSE_RANK() OVER(ORDER BY SUM(s.Sales) DESC) AS SalesRank
FROM Sales s
INNER JOIN Products p
ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY SalesRank;
GO