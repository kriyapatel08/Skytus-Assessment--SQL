from datetime import datetime

# ======================================================
# Task 1 : Find Nth Highest Salary
# ======================================================

print("=" * 50)
print("TASK 1 : Find Nth Highest Salary")
print("=" * 50)

employees = [
    ("Amit", 50000),
    ("Rahul", 70000),
    ("Neha", 60000),
    ("Priya", 70000),
    ("Rohan", 80000)
]

n = 2

salaries = sorted(set(salary for name, salary in employees), reverse=True)

print("Employees:")
for name, salary in employees:
    print(f"{name:<10} : {salary}")

print(f"\n{n} Highest Salary = {salaries[n-1]}")


# ======================================================
# Task 2 : Remove Duplicate Records
# ======================================================

print("\n" + "=" * 50)
print("TASK 2 : Remove Duplicate Records")
print("=" * 50)

employees = [
    ("Amit", 50000),
    ("Rahul", 60000),
    ("Amit", 50000),
    ("Neha", 70000),
    ("Rahul", 60000)
]

print("Original Records:")
for emp in employees:
    print(emp)

unique = list(dict.fromkeys(employees))

print("\nRecords After Removing Duplicates:")
for emp in unique:
    print(emp)


# ======================================================
# Task 3 : Find Common Records in Two Tables
# ======================================================

print("\n" + "=" * 50)
print("TASK 3 : Find Common Records in Two Tables")
print("=" * 50)

tableA = [
    (1, "Amit"),
    (2, "Rahul"),
    (3, "Neha")
]

tableB = [
    (2, "Rahul"),
    (3, "Neha"),
    (4, "Priya")
]

common = list(set(tableA).intersection(set(tableB)))

print("Common Records:")
for record in common:
    print(record)


# ======================================================
# Task 4 : Find Employees Hired in Last 6 Months
# ======================================================

print("\n" + "=" * 50)
print("TASK 4 : Employees Hired in Last 6 Months")
print("=" * 50)

employees = [
    ("Amit", "2026-05-10"),
    ("Rahul", "2025-12-20"),
    ("Neha", "2026-03-15"),
    ("Priya", "2025-08-01")
]

today = datetime.today()

for name, date in employees:
    hire_date = datetime.strptime(date, "%Y-%m-%d")

    months = (today.year - hire_date.year) * 12 + (today.month - hire_date.month)

    if months <= 6:
        print(f"{name:<10} : {date}")


# ======================================================
# Task 5 : Find Continuous Duplicate Values
# ======================================================

print("\n" + "=" * 50)
print("TASK 5 : Find Continuous Duplicate Values")
print("=" * 50)

values = ["A", "A", "B", "B", "B", "C", "A", "A"]

print("Values :", values)

print("\nContinuous Duplicate Values:")

for i in range(len(values) - 1):
    if values[i] == values[i + 1]:
        if i == 0 or values[i] != values[i - 1]:
            print(values[i])

print("\n" + "=" * 50)
print("All Tasks Executed Successfully")
print("=" * 50)