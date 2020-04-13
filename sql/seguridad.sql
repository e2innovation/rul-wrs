USE [RUL-WRS]
GO

IF EXISTS (SELECT name FROM master.sys.server_principals WHERE name = 'RulWrs')
   DROP LOGIN [RulWrs]
GO

 CREATE LOGIN [RulWrs] WITH PASSWORD = N'<CHANGE_PASSWORD>'

IF EXISTS (SELECT * FROM sys.database_principals WHERE name = N'RulWrs')
    DROP USER RulWrs
GO

CREATE USER RulWrs FOR LOGIN RulWrs;
GO

EXEC sp_addrolemember 'db_datareader', 'RulWrs'

EXEC sp_addrolemember 'db_datawriter', 'RulWrs'


IF EXISTS (select * from sys.database_principals where name='db_executor' and Type = 'R')
	DROP ROLE db_executor
GO

CREATE ROLE db_executor;
GRANT EXECUTE TO db_executor;
GO

EXEC sp_addrolemember 'db_executor', 'RulWrs'
