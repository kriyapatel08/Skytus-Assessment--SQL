import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
)
""")

# Create departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT,
    dept_name VARCHAR(50)
)
""")

# Remove old data
cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")

# Insert departments
departments_data = [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance")
]

cursor.executemany(
    "INSERT INTO departments VALUES (?, ?)",
    departments_data
)

# Insert employees
employees_data = [
    (101, "Kriya", 2, 60000),
    (102, "Rahul", 1, 45000),
    (103, "Priya", 2, 75000),
    (104, "Amit", 3, 55000),
    (105, "Neha", 2, 65000),
    (106, "Rohan", 3, 50000)
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?)",
    employees_data
)

conn.commit()

# Task 1: Employees earning more than average salary
print("\n----- Employees Earning More Than Average Salary -----")

cursor.execute("""
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
""")

for row in cursor.fetchall():
    print(row)

# Task 2: Department with highest total salary
print("\n----- Department with Highest Total Salary -----")

cursor.execute("""
SELECT dept_name
FROM departments
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    GROUP BY dept_id
    ORDER BY SUM(salary) DESC
    LIMIT 1
)
""")

for row in cursor.fetchall():
    print(row)

# Task 3: Employee with second highest salary
print("\n----- Employee with Second Highest Salary -----")

cursor.execute("""
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
)
""")

for row in cursor.fetchall():
    print(row)

# Task 4: Employees working in same department as Amit
print("\n----- Employees Working in Same Department as Amit -----")

cursor.execute("""
SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
)
AND emp_name <> 'Amit'
""")

for row in cursor.fetchall():
    print(row)

conn.close()