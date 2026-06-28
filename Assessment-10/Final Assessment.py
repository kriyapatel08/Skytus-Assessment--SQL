import pyodbc

# ===========================
# SQL Server Connection
# ===========================

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=KRIYA\\SQLEXPRESS;'
    'DATABASE=InterviewDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# ==========================================
# Task 1 : Find 2nd Highest Salary
# ==========================================

print("=" * 50)
print("TASK 1 : Find 2nd Highest Salary")
print("=" * 50)

query = """
WITH SalaryRank AS
(
SELECT Salary,
DENSE_RANK() OVER(ORDER BY Salary DESC) AS RankNo
FROM Employees
)
SELECT Salary
FROM SalaryRank
WHERE RankNo = 2;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print("2nd Highest Salary :", row.Salary)


# ==========================================
# Task 2 : Remove Duplicate Records
# ==========================================

print("\n" + "=" * 50)
print("TASK 2 : Remove Duplicate Records")
print("=" * 50)

query = """
WITH CTE AS
(
SELECT *,
ROW_NUMBER() OVER(PARTITION BY Name,Salary ORDER BY ID) RN
FROM EmployeeDuplicate
)
DELETE FROM CTE
WHERE RN>1;
"""

cursor.execute(query)
conn.commit()

cursor.execute("SELECT * FROM EmployeeDuplicate")

print("Records After Removing Duplicates:\n")

for row in cursor.fetchall():
    print(row)


# ==========================================
# Task 3 : Common Records
# ==========================================

print("\n" + "=" * 50)
print("TASK 3 : Common Records")
print("=" * 50)

query = """
SELECT *
FROM TableA
INTERSECT
SELECT *
FROM TableB;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)


# ==========================================
# Task 4 : Employees Hired Last 6 Months
# ==========================================

print("\n" + "=" * 50)
print("TASK 4 : Employees Hired in Last 6 Months")
print("=" * 50)

query = """
SELECT *
FROM EmployeesHire
WHERE HireDate >= DATEADD(MONTH,-6,GETDATE());
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)


# ==========================================
# Task 5 : Continuous Duplicate Values
# ==========================================

print("\n" + "=" * 50)
print("TASK 5 : Continuous Duplicate Values")
print("=" * 50)

query = """
SELECT DISTINCT L1.Value
FROM Logs L1
JOIN Logs L2
ON L1.ID=L2.ID-1
AND L1.Value=L2.Value;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row.Value)

cursor.close()
conn.close()

print("\n" + "=" * 50)
print("All Tasks Executed Successfully")
print("=" * 50)