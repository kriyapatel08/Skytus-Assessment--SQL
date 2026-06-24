import sqlite3

# Connect to database
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
)
""")

# Create Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(50),
    amount INT,
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
)
""")

# Clear previous data
cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM users")

# Insert Users
users_data = [
    (1, "Kriya", "kriya@gmail.com", "pass123"),
    (2, "Rahul", "rahul@gmail.com", "rahul123"),
    (3, "Priya", "priya@gmail.com", "priya123")
]

cursor.executemany(
    "INSERT INTO users VALUES (?, ?, ?, ?)",
    users_data
)

# Insert Orders
orders_data = [
    (101, 1, "Laptop", 55000),
    (102, 1, "Mouse", 1000),
    (103, 2, "Keyboard", 2500),
    (104, 3, "Monitor", 15000)
]

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    orders_data
)

conn.commit()

# Create Index
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_email
ON users(email)
""")

# Drop view if already exists
cursor.execute("DROP VIEW IF EXISTS user_order_summary")

# Create View
cursor.execute("""
CREATE VIEW user_order_summary AS
SELECT
    users.user_id,
    users.username,
    COUNT(orders.order_id) AS total_orders,
    SUM(orders.amount) AS total_amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
GROUP BY users.user_id, users.username
""")

# Display View
print("\n----- User Order Summary -----")

cursor.execute("SELECT * FROM user_order_summary")

for row in cursor.fetchall():
    print(row)

conn.close()