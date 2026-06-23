CREATE TABLE employees(
    emp_id INT,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

CREATE TABLE departments(
    dept_id INT,
    dept_name VARCHAR(50)
);

-- Insert Data
INSERT INTO departments VALUES
(1,'HR'),
(2,'IT'),
(3,'Finance');

INSERT INTO employees VALUES
(101,'Kriya',2,60000),
(102,'Rahul',1,45000),
(103,'Priya',2,75000),
(104,'Amit',3,55000),
(105,'Neha',2,65000),
(106,'Rohan',NULL,50000);

-- Task 1: Display Employee Name with Department Name

SELECT emp_name, dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;


-- Task 2: Display Employees Earning More Than 50000

SELECT *
FROM employees
WHERE salary > 50000;

-- Task 3: Display Department-wise Total Salary

SELECT dept_name, SUM(salary)
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
GROUP BY dept_name;

-- Task 4: Display Departments with More Than 2 Employees

SELECT dept_name, COUNT(emp_id)
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
GROUP BY dept_name
HAVING COUNT(emp_id) > 2;

-- Task 5: Display Employees Without a Department

SELECT emp_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id
WHERE dept_name IS NULL;
