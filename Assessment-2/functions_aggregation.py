import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
)
""")

# Insert sample data
students = [
    (1, "Kriya", "CSE", 2, 85),
    (2, "Rahul", "IT", 3, 72),
    (3, "Priya", "CSE", 1, 91),
    (4, "Amit", "ECE", 4, 68),
    (5, "Neha", "CSE", 2, 78)
]

cursor.execute("DELETE FROM students")
cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
    students
)

conn.commit()

import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Count total students
cursor.execute("SELECT COUNT(*) FROM students")
print("Total Students =", cursor.fetchone()[0])

# Average marks
cursor.execute("SELECT AVG(marks) FROM students")
print("Average Marks =", cursor.fetchone()[0])

# Highest and Lowest marks
cursor.execute("SELECT MAX(marks), MIN(marks) FROM students")
result = cursor.fetchone()
print("Highest Marks =", result[0])
print("Lowest Marks =", result[1])

# Department-wise average marks
print("\nDepartment-wise Average Marks:")
cursor.execute("""
SELECT department, AVG(marks)
FROM students
GROUP BY department
""")

for row in cursor.fetchall():
    print(row)

# Departments with average marks > 70
print("\nDepartments with Average Marks > 70:")
cursor.execute("""
SELECT department, AVG(marks)
FROM students
GROUP BY department
HAVING AVG(marks) > 70
""")

for row in cursor.fetchall():
    print(row)

conn.close()