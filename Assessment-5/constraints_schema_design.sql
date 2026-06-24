-- Assessment 5: Constraints & Schema Design
-- 1.Users table

-- Primary Key
-- Unique Email
-- Password NOT NULL
USE ecommerce_db;
GO

-- Create Users Table 

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create Orders Table with Foreign Key
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),

    CONSTRAINT FK_UserOrder
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

-- insert sample data
INSERT INTO users (user_id, username, email, password)
VALUES
(1, 'Kriya', 'kriya@gmail.com', 'pass123'),
(2, 'Rahul', 'rahul@gmail.com', 'pass456'),
(3, 'Priya', 'priya@gmail.com', 'pass789');

INSERT INTO orders (order_id, user_id, order_date, amount)
VALUES
(105, 1, '2026-06-24', 500.00),
(106, 2, '2026-06-24', 750.00),
(107, 3, '2026-06-24', 900.00);

-- Create View for User Order Summary
DROP VIEW IF EXISTS user_order_summary;
GO

CREATE VIEW user_order_summary AS
SELECT
    u.user_id,
    u.username,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY
    u.user_id,
    u.username,
    u.email;
GO

-- Create Index on Email

IF NOT EXISTS (
    SELECT *
    FROM sys.indexes
    WHERE name = 'idx_email'
      AND object_id = OBJECT_ID('users')
)
BEGIN
    CREATE INDEX idx_email
    ON users(email);
END

-- Verify Index
EXEC sp_helpindex 'users';

-- Display view output
SELECT * FROM user_order_summary;

-- Display Users
SELECT * FROM users;

-- Display Orders
SELECT * FROM orders;