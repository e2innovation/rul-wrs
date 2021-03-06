USE master
GO

IF DB_ID('RUL-WRS') IS NULL 
BEGIN
	CREATE DATABASE [RUL-WRS] ON  PRIMARY
	(
		NAME = N'RUL-WRS',
		FILENAME = N'D:\RUL_WRS\BD\RUL-WRS.mdf',
		SIZE = 2GB,
		MAXSIZE = 8GB,
		FILEGROWTH = 1GB
	)
	LOG ON
	(
		NAME = N'RUL-WRS_log',
		FILENAME = N'D:\RUL_WRS\BD\RUL-WRS_log.ldf',
		SIZE = 1GB,
		MAXSIZE = 2GB,
		FILEGROWTH = 10%
	)	
END
