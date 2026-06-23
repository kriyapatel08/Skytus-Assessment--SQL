-- Create Employees Table
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

-- Create Departments Table
CREATE TABLE departments (
    dept_id INT,
    dept_name VARCHAR(50)
);

-- Insert Data into Departments Table
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

-- Insert Data into Employees Table
INSERT INTO employees VALUES
(101, 'Kriya', 2, 60000),
(102, 'Rahul', 1, 45000),
(103, 'Priya', 2, 75000),
(104, 'Amit', 3, 55000),
(105, 'Neha', 2, 65000),
(106, 'Rohan', 3, 50000);


-- Task 1: Employees earning more than average salary


SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- Task 2: Department with highest total salary


SELECT dept_name
FROM departments
WHERE dept_id = (
    SELECT TOP 1 dept_id
    FROM employees
    GROUP BY dept_id
    ORDER BY SUM(salary) DESC
);


-- Task 3: Employee with second highest salary


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


-- Task 4: Employees working in same department as Amit


SELECT *
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
)
AND emp_name <> 'Amit';