import sqlite3

# Connect to database
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

# Insert Sample Data
customers = [
    (1, 'Rahul', 'Mumbai'),
    (2, 'Priya', 'Delhi'),
    (3, 'Amit', 'Ahmedabad'),
    (4, 'Neha', 'Surat'),
    (5, 'Karan', 'Mumbai')
]

orders = [
    (1001, 1, '2025-01-10', 53000),
    (1002, 2, '2025-01-15', 20000),
    (1003, 1, '2025-02-05', 1500),
    (1004, 3, '2025-02-20', 23000),
    (1005, 5, '2025-03-01', 50000)
]

products = [
    (101, 'Laptop', 50000),
    (102, 'Mobile', 20000),
    (103, 'Headphones', 3000),
    (104, 'Keyboard', 1500)
]

order_items = [
    (1001, 101, 1),
    (1001, 103, 1),
    (1002, 102, 1),
    (1003, 104, 1),
    (1004, 102, 1),
    (1004, 103, 1),
    (1005, 101, 1)
]

cursor.executemany(
    "INSERT OR IGNORE INTO customers VALUES (?, ?, ?)",
    customers
)

cursor.executemany(
    "INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?)",
    orders
)

cursor.executemany(
    "INSERT OR IGNORE INTO products VALUES (?, ?, ?)",
    products
)

cursor.executemany(
    "INSERT OR IGNORE INTO order_items VALUES (?, ?, ?)",
    order_items
)

conn.commit()

# Task 1: Create Index

print("\nTASK 1: CREATE INDEX")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_orders_customer_id
ON orders(customer_id)
""")

print("Index created successfully.")


# Task 2: Analyze Query

print("\nTASK 2: ANALYZE QUERY")

cursor.execute("""
EXPLAIN QUERY PLAN
SELECT *
FROM orders
WHERE customer_id = 1
""")

for row in cursor.fetchall():
    print(row)

# Task 3: Optimize Join Query
print("\nTASK 3: OPTIMIZED JOIN QUERY")

cursor.execute("""
SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
""")

for row in cursor.fetchall():
    print(row)

# -------------------------
# Task 4: When Index Should Not Be Used
# -------------------------
print("\nTASK 4: SMALL TABLE QUERY")

cursor.execute("""
SELECT *
FROM customers
""")

for row in cursor.fetchall():
    print(row)

print("""
Explanation:
Indexes should not be used on:
1. Small tables.
2. Low-cardinality columns.
3. Frequently updated tables.
4. Rarely searched columns.
5. Tables with too many indexes.
""")

conn.close()

print("\nAssessment Completed Successfully.")