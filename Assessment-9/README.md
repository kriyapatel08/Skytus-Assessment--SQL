# SQL Assessment - Interview SQL Queries & Python Solutions

## Student Information

- **Assessment:** SQL Interview Questions
- **Language:** SQL Server (SSMS) & Python 3
- **Database:** InterviewDB

---

## Objective

The objective of this assessment is to demonstrate SQL querying skills and implement equivalent logic using Python.

---

## Tasks Completed

### Task 1: Find Nth Highest Salary
- Created an Employees table.
- Inserted sample employee records.
- Used `DENSE_RANK()` to find the 2nd highest salary.
- Implemented the same logic in Python.

---

### Task 2: Remove Duplicate Records
- Created a table with duplicate employee records.
- Used `ROW_NUMBER()` and Common Table Expression (CTE) to remove duplicates.
- Implemented duplicate removal using Python.

---

### Task 3: Find Common Records in Two Tables
- Created two sample tables.
- Used `INTERSECT` to retrieve common records.
- Implemented the same using Python `set.intersection()`.

---

### Task 4: Find Employees Hired in Last 6 Months
- Created an employee hiring table.
- Used `DATEADD()` and `GETDATE()` in SQL Server.
- Implemented equivalent date filtering in Python.

---

### Task 5: Find Continuous Duplicate Values
- Created a Logs table.
- Used SQL JOIN to identify continuous duplicate values.
- Implemented the same logic using list traversal in Python.

---

## Project Structure

```
Assessment/
│
├── SQL_Interview_Assessment.sql
├── interview_questions.py
└── README.md
```

---

## Technologies Used

- Microsoft SQL Server (SSMS)
- Python 3.x
- Visual Studio Code

---

## SQL Concepts Used

- CREATE DATABASE
- CREATE TABLE
- INSERT INTO
- SELECT
- DENSE_RANK()
- ROW_NUMBER()
- Common Table Expression (CTE)
- INTERSECT
- INNER JOIN
- DATEADD()
- GETDATE()
- DELETE
- DISTINCT

---

## Python Concepts Used

- Lists
- Tuples
- Sets
- Dictionary
- Loops
- Conditional Statements
- Datetime Module
- List Operations

---

## Expected Output

- Find Nth Highest Salary
- Remove Duplicate Records
- Display Common Records
- Show Employees Hired in Last 6 Months
- Find Continuous Duplicate Values

All tasks execute successfully and display the required results.

---

## Conclusion

This assessment demonstrates the implementation of common SQL interview questions using Microsoft SQL Server along with equivalent Python solutions. The project covers ranking functions, duplicate handling, table comparison, date filtering, and sequence analysis, providing a practical understanding of SQL and Python programming concepts.