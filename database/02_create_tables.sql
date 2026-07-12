USE SalesAnalyticsDB;
GO

/*====================================================
CUSTOMERS
====================================================*/

CREATE TABLE Customers
(
    CustomerID NVARCHAR(30) PRIMARY KEY,
    CustomerName NVARCHAR(150) NOT NULL,
    Segment NVARCHAR(50) NOT NULL
);

GO

/*====================================================
PRODUCTS
====================================================*/

CREATE TABLE Products
(
    ProductID NVARCHAR(50) PRIMARY KEY,
    ProductName NVARCHAR(300) NOT NULL,
    Category NVARCHAR(100) NOT NULL,
    SubCategory NVARCHAR(100) NOT NULL
);

GO

/*====================================================
ORDERS
====================================================*/

CREATE TABLE Orders
(
    OrderID NVARCHAR(30) PRIMARY KEY,
    OrderDate DATE NOT NULL,
    ShipDate DATE NOT NULL,
    ShipMode NVARCHAR(50),
    OrderPriority NVARCHAR(30)
);

GO

/*====================================================
LOCATIONS
====================================================*/

CREATE TABLE Locations
(
    LocationID INT IDENTITY(1,1) PRIMARY KEY,
    Country NVARCHAR(100),
    Market NVARCHAR(100),
    Region NVARCHAR(100),
    State NVARCHAR(100),
    City NVARCHAR(100)
);

GO

/*====================================================
SALES
====================================================*/

CREATE TABLE Sales
(
    RowID INT PRIMARY KEY,

    OrderID NVARCHAR(30),
    CustomerID NVARCHAR(30),
    ProductID NVARCHAR(50),
    LocationID INT,

    Sales DECIMAL(18,2),
    Quantity INT,
    Discount DECIMAL(10,2),
    Profit DECIMAL(18,2),
    ShippingCost DECIMAL(18,2),

    SalesYear INT,
    WeekNum INT,

    CONSTRAINT FK_Sales_Order
        FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID),

    CONSTRAINT FK_Sales_Customer
        FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT FK_Sales_Product
        FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    CONSTRAINT FK_Sales_Location
        FOREIGN KEY (LocationID)
        REFERENCES Locations(LocationID)
);

GO