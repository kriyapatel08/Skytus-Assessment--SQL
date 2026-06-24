import sqlite3

# Connect to database
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    AccountID INTEGER PRIMARY KEY,
    AccountHolder TEXT,
    Balance REAL
)
""")

# Insert sample data
cursor.execute("DELETE FROM Accounts")

cursor.execute("INSERT INTO Accounts VALUES (1, 'John', 5000)")
cursor.execute("INSERT INTO Accounts VALUES (2, 'Alice', 3000)")

conn.commit()

print("Initial Data:")
for row in cursor.execute("SELECT * FROM Accounts"):
    print(row)

# Transaction Example
try:
    conn.execute("BEGIN TRANSACTION")

    # Transfer ₹1000 from John to Alice
    cursor.execute("""
        UPDATE Accounts
        SET Balance = Balance - 1000
        WHERE AccountID = 1
    """)

    cursor.execute("""
        UPDATE Accounts
        SET Balance = Balance + 1000
        WHERE AccountID = 2
    """)

    conn.commit()
    print("\nTransaction Committed Successfully!")

except Exception as e:
    conn.rollback()
    print("\nTransaction Failed!")
    print(e)

print("\nFinal Data:")
for row in cursor.execute("SELECT * FROM Accounts"):
    print(row)

conn.close()