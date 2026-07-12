-- Create Database

IF DB_ID('SalesAnalyticsDB') IS NOT NULL
DROP DATABASE SalesAnalyticsDB;
GO

CREATE DATABASE SalesAnalyticsDB;
GO

USE SalesAnalyticsDB;
GO