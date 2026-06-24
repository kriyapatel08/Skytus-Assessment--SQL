

import sqlite3
import os

# Delete old database if it exists
if os.path.exists("ecommerce.db"):
    os.remove("ecommerce.db")

# Create database
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Create products table
cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL
)
""")

# Create order_items table
cursor.execute("""
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

# Insert customers
customers = [
    (1, "Rahul", "Mumbai"),
    (2, "Priya", "Delhi"),
    (3, "Amit", "Ahmedabad"),
    (4, "Neha", "Surat"),
    (5, "Karan", "Mumbai")
]

cursor.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)

# Insert products
products = [
    (101, "Laptop", 50000),
    (102, "Mobile", 20000),
    (103, "Headphones", 3000),
    (104, "Keyboard", 1500)
]

cursor.executemany(
    "INSERT INTO products VALUES (?, ?, ?)",
    products
)

# Insert orders
orders = [
    (1001, 1, "2025-01-10", 53000),
    (1002, 2, "2025-01-15", 20000),
    (1003, 1, "2025-02-05", 1500),
    (1004, 3, "2025-02-20", 23000),
    (1005, 5, "2025-03-01", 50000)
]

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    orders
)

# Insert order items
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
    "INSERT INTO order_items VALUES (?, ?, ?)",
    order_items
)

conn.commit()

# TASK 1
print("\n=== Total Orders Per Customer ===")
cursor.execute("""
SELECT c.customer_id,
       c.name,
       COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC
""")

for row in cursor.fetchall():
    print(row)

# TASK 2
print("\n=== Customers Who Never Placed an Order ===")
cursor.execute("""
SELECT c.customer_id,
       c.name,
       c.city
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
""")

for row in cursor.fetchall():
    print(row)

# TASK 3
print("\n=== Highest Selling Product ===")
cursor.execute("""
SELECT p.product_name,
       SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_sold DESC
LIMIT 1
""")

for row in cursor.fetchall():
    print(row)

# TASK 4
print("\n=== Monthly Sales Report ===")
cursor.execute("""
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(amount) AS total_sales
FROM orders
GROUP BY month
ORDER BY month
""")

for row in cursor.fetchall():
    print(row)

# TASK 5
print("\n=== Customers With Purchase > 50000 ===")
cursor.execute("""
SELECT c.customer_id,
       c.name,
       SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000
""")

for row in cursor.fetchall():
    print(row)

# TASK 6
print("\n=== Top 3 Cities By Revenue ===")
cursor.execute("""
SELECT c.city,
       SUM(o.amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC
LIMIT 3
""")

for row in cursor.fetchall():
    print(row)

conn.close()