
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students VALUES
(1, 'Amit', 'CSE', 1, 85),
(2, 'Priya', 'IT', 2, 72),
(3, 'Rahul', 'CSE', 3, 91),
(4, 'Sneha', 'ECE', 2, 68),
(5, 'Karan', 'CSE', 1, 78),
(6, 'Neha', 'IT', 3, 95);

-- 1. Display all student records

SELECT * FROM students;

-- 2. Display only name and department
SELECT name, department
FROM students;

-- 3. Find students with marks greater than 75

SELECT *
FROM students
WHERE marks > 75;

-- 4. Display students from CSE department

SELECT *
FROM students
WHERE department = 'CSE';

-- 5. Sort students by marks (descending)

SELECT *
FROM students
ORDER BY marks DESC;

-- 6. Display Top 3 Scorers

SELECT TOP 3 *
FROM students
ORDER BY marks DESC;


