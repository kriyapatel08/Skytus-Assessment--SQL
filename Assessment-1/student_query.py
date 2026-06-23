import sqlite3

# Connect to database (creates database file if it doesn't exist)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
)
""")

# Insert sample records
cursor.execute("DELETE FROM students")

students_data = [
    (1, "Kriya", "CSE", 2, 85),
    (2, "Rahul", "IT", 3, 72),
    (3, "Priya", "CSE", 1, 91),
    (4, "Amit", "ECE", 4, 68),
    (5, "Neha", "CSE", 2, 78)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
    students_data
)

conn.commit()

# 1. Display all student records
print("1. All Student Records")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 2. Display only name and department
print("\n2. Name and Department")
cursor.execute("SELECT name, department FROM students")
for row in cursor.fetchall():
    print(row)

# 3. Find students with marks greater than 75
print("\n3. Students with Marks > 75")
cursor.execute("SELECT * FROM students WHERE marks > 75")
for row in cursor.fetchall():
    print(row)

# 4. Display students from CSE department
print("\n4. CSE Department Students")
cursor.execute("SELECT * FROM students WHERE department = 'CSE'")
for row in cursor.fetchall():
    print(row)

# 5. Sort students by marks (descending)
print("\n5. Students Sorted by Marks (Descending)")
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
for row in cursor.fetchall():
    print(row)

# 6. Display top 3 scorers
print("\n6. Top 3 Scorers")
cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
for row in cursor.fetchall():
    print(row)

conn.close()