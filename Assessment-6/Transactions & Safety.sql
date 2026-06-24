-- Create Database
CREATE DATABASE Banking_DB;
GO

USE Banking_DB;
GO

-- Create Accounts Table
CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    AccountHolder VARCHAR(100),
    Balance DECIMAL(10,2)
);
GO

-- Insert Sample Data
INSERT INTO Accounts VALUES
(1, 'Kriya', 5000.00),
(2, 'Mili', 3000.00);
GO

-- Task 1: Start a Transaction

BEGIN TRANSACTION;

INSERT INTO Accounts
VALUES (3, 'Riya', 2000.00);

SELECT * FROM Accounts;

-- Task 2: Rollback Changes

ROLLBACK;

SELECT * FROM Accounts;
GO

-- Task 3: Commit Valid Transaction

BEGIN TRANSACTION;

INSERT INTO Accounts
VALUES (3, 'Riya', 2000.00);

COMMIT;

SELECT * FROM Accounts;
GO

-- Task 4: Money Transfer Transaction
BEGIN TRANSACTION;

UPDATE Accounts
SET Balance = Balance - 1000
WHERE AccountID = 1;

UPDATE Accounts
SET Balance = Balance + 1000
WHERE AccountID = 2;

COMMIT;

SELECT * FROM Accounts;
GO

