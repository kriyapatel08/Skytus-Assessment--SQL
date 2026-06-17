-- 1. Count Total Number of Students

SELECT COUNT(*) AS Total_Students
FROM students;

-- 2. Find Average Marks of Students

SELECT AVG(marks) AS Average_Marks
FROM students;

-- 3. find highest and Lowest marks

SELECT
MAX(marks) AS Highest_Marks,
MIN(marks) AS Lowest_Marks
FROM students;

-- 4. Find Department-wise Average Marks

SELECT department,
  AVG(marks) AS Average_marks
FROM students
GROUP BY department;

-- 5. Display Departments Where Average Marks > 70

SELECT department,
  AVG(marks) AS Average_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
