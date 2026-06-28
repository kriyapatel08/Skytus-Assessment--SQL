CREATE DATABASE InterviewDB;
GO

USE InterviewDB;
GO

--Write Query to Find Nth Highest Salary

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Salary DECIMAL(10,2)
);

INSERT INTO Employees VALUES
(1,'Amit',50000),
(2,'Rahul',70000),
(3,'Neha',60000),
(4,'Priya',70000),
(5,'Rohan',80000);

--Task-1 Find 2nd Highest Salary
WITH SalaryRank AS
(
    SELECT Salary,
           DENSE_RANK() OVER(ORDER BY Salary DESC) AS RankNo
    FROM Employees
)
SELECT Salary
FROM SalaryRank
WHERE RankNo = 2;

--Task-2 Remove Duplicate Records
CREATE TABLE EmployeeDuplicate
(
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Salary INT
);

INSERT INTO EmployeeDuplicate VALUES
(1,'Amit',50000),
(2,'Rahul',60000),
(3,'Amit',50000),
(4,'Neha',70000),
(5,'Rahul',60000);

WITH CTE AS
(
SELECT *,
ROW_NUMBER() OVER
(PARTITION BY Name, Salary ORDER BY ID) AS RN
FROM EmployeeDuplicate
)

DELETE FROM CTE
WHERE RN > 1;

SELECT * FROM EmployeeDuplicate;

--Task-3 Find Records Common in Two Tables

CREATE TABLE TableA
(
ID INT,
Name VARCHAR(30)
);

CREATE TABLE TableB
(
ID INT,
Name VARCHAR(30)
);

INSERT INTO TableA VALUES
(1,'Amit'),
(2,'Rahul'),
(3,'Neha');

INSERT INTO TableB VALUES
(2,'Rahul'),
(3,'Neha'),
(4,'Priya');

SELECT *
FROM TableA
INTERSECT
SELECT *
FROM TableB;

--Task-4 Find Employees Hired in Last 6 Months

CREATE TABLE EmployeesHire
(
EmpID INT,
EmpName VARCHAR(30),
HireDate DATE
);

INSERT INTO EmployeesHire VALUES
(1,'Amit','2026-05-10'),
(2,'Rahul','2025-12-20'),
(3,'Neha','2026-03-15'),
(4,'Priya','2025-08-01');

SELECT *
FROM EmployeesHire
WHERE HireDate >= DATEADD(MONTH,-6,GETDATE());

--Task-5 Find Continuous Duplicate Values

CREATE TABLE Logs
(
ID INT,
Value VARCHAR(20)
);

INSERT INTO Logs VALUES
(1,'A'),
(2,'A'),
(3,'B'),
(4,'B'),
(5,'B'),
(6,'C'),
(7,'A'),
(8,'A');

SELECT DISTINCT L1.Value
FROM Logs L1
JOIN Logs L2
ON L1.ID = L2.ID - 1
AND L1.Value = L2.Value;

