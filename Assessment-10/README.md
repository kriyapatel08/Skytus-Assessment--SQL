# SQL Interview Assessment

## Student Details

- **Student Name:** Patel Kriya
- **Assessment:** SQL Interview Questions
- **Database:** InterviewDB
- **Programming Language:** Python 3
- **SQL Server:** Microsoft SQL Server (SSMS)

---

# Project Overview

This assessment demonstrates solutions to five commonly asked SQL interview questions along with their equivalent Python implementations.

The project includes:
- SQL queries for each task
- Python implementation for each task
- Sample data and expected outputs

---

# Tasks Implemented

## Task 1: Find Nth Highest Salary

### SQL
- Created the `Employees` table.
- Inserted sample employee records.
- Used the `DENSE_RANK()` window function to retrieve the 2nd highest salary.

### Python
- Stored employee records in a list.
- Used `set()` and `sorted()` to determine the Nth highest salary.

---

## Task 2: Remove Duplicate Records

### SQL
- Created the `EmployeeDuplicate` table.
- Used `ROW_NUMBER()` with a Common Table Expression (CTE) to identify and delete duplicate records.

### Python
- Removed duplicate records using `dict.fromkeys()` while preserving insertion order.

---

## Task 3: Find Common Records in Two Tables

### SQL
- Created `TableA` and `TableB`.
- Used the `INTERSECT` operator to find common records.

### Python
- Used `set.intersection()` to identify records present in both lists.

---

## Task 4: Find Employees Hired in Last 6 Months

### SQL
- Created the `EmployeesHire` table.
- Used `DATEADD()` and `GETDATE()` to retrieve employees hired within the last six months.

### Python
- Used the `datetime` module to compare hire dates with the current date.

---

## Task 5: Find Continuous Duplicate Values

### SQL
- Created the `Logs` table.
- Used SQL JOIN operations to identify continuous duplicate values.

### Python
- Traversed a list and compared adjacent elements to detect continuous duplicates.

---

# Project Structure

```
SQL-Interview-Assessment/
│
├── SQL_Interview_Assessment.sql
├── interview_questions.py
└── README.md
```

---

# Technologies Used

- Microsoft SQL Server Management Studio (SSMS)
- Python 3.x
- Visual Studio Code

---

# SQL Concepts Used

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

# Python Concepts Used

- Lists
- Tuples
- Sets
- Dictionaries
- Loops
- Conditional Statements
- Datetime Module

---

# Expected Output

The program successfully performs the following operations:

- Find the Nth Highest Salary
- Remove Duplicate Records
- Display Common Records from Two Tables
- Display Employees Hired in the Last Six Months
- Identify Continuous Duplicate Values

Each task displays its output separately with proper formatting.

---

# How to Run

## SQL

1. Open Microsoft SQL Server Management Studio (SSMS).
2. Open the `SQL_Interview_Assessment.sql` file.
3. Execute the script.
4. View the output for each task in the Results pane.

## Python

1. Open the project in Visual Studio Code.
2. Run the `interview_questions.py` file using:

```bash
python interview_questions.py
```

3. The output for all five tasks will be displayed automatically.

---

# Conclusion

This assessment demonstrates practical SQL querying techniques and their equivalent Python implementations. It covers ranking functions, duplicate record handling, table comparison, date-based filtering, and continuous duplicate detection, showcasing fundamental database querying and Python programming skills.