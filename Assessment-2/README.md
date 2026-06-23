# Assessment 2 - Functions and Aggregation

## Objective

To perform aggregate operations on student records using SQL and Python.

## Topics Covered

- COUNT()
- AVG()
- MAX()
- MIN()
- GROUP BY
- HAVING

## Files

```
functions_aggregation.py
students.db
```

## Sample Queries

```sql
SELECT COUNT(*) FROM students;

SELECT AVG(marks) FROM students;

SELECT MAX(marks), MIN(marks)
FROM students;

SELECT department, AVG(marks)
FROM students
GROUP BY department;

SELECT department, AVG(marks)
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
```

## Technologies Used

- Python
- SQLite3
- Visual Studio Code