IF OBJECT_ID('students', 'U') IS NOT NULL
    DROP TABLE students;

CREATE TABLE students(
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

-- 1. Display all student records
SELECT * FROM students;

-- -- 2. Display only name and department
-- SELECT name, department FROM students;

-- -- 3. Find students with marks greater than 75
-- SELECT * FROM students
-- WHERE marks > 75;

-- -- 4. Display students from CSE department
-- SELECT * FROM students
-- WHERE department = 'CSE';

-- -- 5. Sort students by marks (descending)
-- SELECT * FROM students
-- ORDER BY marks DESC;

-- -- 6. Display top 3 scorers
-- SELECT * FROM students
-- ORDER BY marks DESC;
-- -- LIMIT 3;      -- MySQL/PostgreSQL

-- -- For SQL Server:
-- SELECT TOP 3 * FROM students
-- ORDER BY marks DESC;

select * from students where department = 'CSE' and marks > 75;
