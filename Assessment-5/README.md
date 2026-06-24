# Assessment 5 - Constraints & Schema Design

## Objective

To understand database constraints and schema design concepts using SQL and Python.

---

## Tasks

- Create users table with:
  - Primary Key
  - Unique Email
  - NOT NULL Password

- Add Foreign Key between orders and users

- Create Index on email column

- Create View to display user order summary

---

## Database

ecommerce.db

### Users Table

| Column | Type | Constraint |
|----------|------|------------|
| user_id | INT | PRIMARY KEY |
| username | VARCHAR(50) | - |
| email | VARCHAR(100) | UNIQUE |
| password | VARCHAR(100) | NOT NULL |

### Orders Table

| Column | Type | Constraint |
|----------|------|------------|
| order_id | INT | PRIMARY KEY |
| user_id | INT | FOREIGN KEY |
| product_name | VARCHAR(50) | - |
| amount | INT | - |

---

## Concepts Covered

- PRIMARY KEY
- UNIQUE Constraint
- NOT NULL Constraint
- FOREIGN KEY
- INDEX
- VIEW
- GROUP BY
- Aggregate Functions

---

## Files

```
Assessment-5/
│
├── constraints_schema_design.py
├── constraints_schema_design.sql
├── ecommerce.db
└── README.md
```

---

## How to Run

### Run Python File

```bash
python constraints_schema_design.py
```

### Run SQL File

Execute:

```text
constraints_schema_design.sql
```

in SQLite or SQL Server.

---

## Technologies Used

- Python 3
- SQLite3
- SQL
- Visual Studio Code

---

## Author

Kriya Patel