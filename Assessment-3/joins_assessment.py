import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INT,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
)
""")

# Create departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments(
    dept_id INT,
    dept_name VARCHAR(50)
)
""")

# Delete previous records
cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")

# Insert data into departments
departments_data = [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance")
]

cursor.executemany(
    "INSERT INTO departments VALUES (?, ?)",
    departments_data
)

# Insert data into employees
employees_data = [
    (101, "Kriya", 2, 60000),
    (102, "Rahul", 1, 45000),
    (103, "Priya", 2, 75000),
    (104, "Amit", 3, 55000),
    (105, "Neha", 2, 65000),
    (106, "Rohan", None, 50000)
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?)",
    employees_data
)

conn.commit()

# Task 1: Employee name with department name
print("\n----- Employee Name with Department Name -----")

cursor.execute("""
SELECT emp_name, dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
""")

for row in cursor.fetchall():
    print(row)

# Task 2: Employees earning more than 50000
print("\n----- Employees Earning More Than 50000 -----")

cursor.execute("""
SELECT *
FROM employees
WHERE salary > 50000
""")

for row in cursor.fetchall():
    print(row)

# Task 3: Department-wise total salary
print("\n----- Department-wise Total Salary -----")

cursor.execute("""
SELECT dept_name, SUM(salary)
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
GROUP BY dept_name
""")

for row in cursor.fetchall():
    print(row)

# Task 4: Departments with more than 2 employees
print("\n----- Departments with More Than 2 Employees -----")

cursor.execute("""
SELECT dept_name, COUNT(emp_id)
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
GROUP BY dept_name
HAVING COUNT(emp_id) > 2
""")

for row in cursor.fetchall():
    print(row)

# Task 5: Employees without a department
print("\n----- Employees Without Department -----")

cursor.execute("""
SELECT emp_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id
WHERE dept_name IS NULL
""")

for row in cursor.fetchall():
    print(row)

conn.close()