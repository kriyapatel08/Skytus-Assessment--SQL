# Assessment 4 - Subqueries

## Objective

To understand and implement SQL Subqueries using Python and SQLite.

## Database

**company_db**

---

## Tables

### employees

| Column Name | Data Type |
|-------------|-----------|
| emp_id | INT |
| emp_name | VARCHAR(50) |
| dept_id | INT |
| salary | INT |

### departments

| Column Name | Data Type |
|-------------|-----------|
| dept_id | INT |
| dept_name | VARCHAR(50) |

---

## Topics Covered

- Single Row Subqueries
- Nested Queries
- Aggregate Functions
- GROUP BY
- ORDER BY
- MAX()
- AVG()

---

## Tasks

### 1. Find employees earning more than average salary

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

### 2. Find department with highest total salary

```sql
SELECT dept_name
FROM departments
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    GROUP BY dept_id
    ORDER BY SUM(salary) DESC
    LIMIT 1
);
```

---

### 3. Display employee with second highest salary

```sql
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);
```

---

### 4. Display employees working in the same department as "Amit"

```sql
SELECT *
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
)
AND emp_name <> 'Amit';
```

---

## Files

```
Assessment-4/
│
├── subqueries_assessment.py
├── subqueries_assessment.sql
├── company.db
└── README.md
```

---

## Technologies Used

- Python 3
- SQLite3
- SQL
- Visual Studio Code

---

## How to Run

### Run Python File

```bash
python subqueries_assessment.py
```

### Execute SQL File

Run the queries in:

```text
subqueries_assessment.sql
```

using SQLite or SQL Server.

---

## Concepts Learned

- Writing nested queries
- Using aggregate functions inside subqueries
- Finding second highest values
- Using `IN` operator with subqueries
- Filtering data using subqueries

---

## Author

**Kriya Patel**