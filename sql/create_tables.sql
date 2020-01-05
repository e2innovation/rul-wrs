USE [RUL-WRS]
GO

IF OBJECT_ID('dbo.Machine') IS NULL
	CREATE TABLE dbo.Machine
	(
		id VARCHAR(256) PRIMARY KEY,
		[type] VARCHAR(256),
		[description] VARCHAR(4096),
		[disabled] BIT
	);
GO