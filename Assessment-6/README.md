# Assessment 6 - Transactions & Safety

## Objective
The purpose of this assessment is to understand and implement database transactions to ensure data consistency and safety. The project demonstrates how transactions can be started, committed, and rolled back when necessary.

---

## Technologies Used

- Python 3
- SQLite (sqlite3 module)
- SQL

---

## Database Table

### Accounts

| Column Name | Data Type |
|------------|------------|
| AccountID | INTEGER |
| AccountHolder | TEXT |
| Balance | REAL |

---

## Tasks Performed

### 1. Start a Transaction

A transaction is started using:

```python
conn.execute("BEGIN TRANSACTION")
```

This ensures that multiple database operations are treated as a single unit.

---

### 2. Insert Records into Accounts Table

Sample account records are inserted:

```python
cursor.execute("INSERT INTO Accounts VALUES (1, 'John', 5000)")
cursor.execute("INSERT INTO Accounts VALUES (2, 'Alice', 3000)")
```

---

### 3. Rollback Changes

If any error occurs during the transaction, all changes are cancelled using:

```python
conn.rollback()
```

This restores the database to its previous state.

---

### 4. Commit Valid Transactions

If all operations are completed successfully, the changes are permanently saved using:

```python
conn.commit()
```

---

### 5. Money Transfer Using Transaction

A money transfer is performed between two accounts.

#### Deduct Amount from Sender

```python
cursor.execute("""
UPDATE Accounts
SET Balance = Balance - 1000
WHERE AccountID = 1
""")
```

#### Add Amount to Receiver

```python
cursor.execute("""
UPDATE Accounts
SET Balance = Balance + 1000
WHERE AccountID = 2
""")
```

#### Commit Transaction

```python
conn.commit()
```

---

## Program Flow

1. Create database connection.
2. Create Accounts table.
3. Insert sample records.
4. Display initial account balances.
5. Start transaction.
6. Transfer money from one account to another.
7. Commit transaction if successful.
8. Rollback transaction if any error occurs.
9. Display updated account balances.

---

## Expected Output

### Before Transaction

| AccountID | AccountHolder | Balance |
|------------|---------------|----------|
| 1 | John | 5000 |
| 2 | Alice | 3000 |

### After Transaction

| AccountID | AccountHolder | Balance |
|------------|---------------|----------|
| 1 | John | 4000 |
| 2 | Alice | 4000 |

---

## Conclusion

This assessment demonstrates the importance of transactions in database systems. Transactions ensure that operations are executed safely and maintain data integrity. Using COMMIT and ROLLBACK helps prevent inconsistent data when errors occur during execution.