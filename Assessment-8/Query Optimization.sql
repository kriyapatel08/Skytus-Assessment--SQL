
USE ecommerce_db;
GO

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Create Orders Table
CREATE TABLE orderss (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Create Order_Items Table
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orderss(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- customers
INSERT INTO customers VALUES
(1,'Rahul','Mumbai'),
(2,'Priya','Delhi'),
(3,'Amit','Ahmedabad'),
(4,'Neha','Surat'),
(5,'Karan','Mumbai');

-- products
INSERT INTO products VALUES
(101,'Laptop',50000),
(102,'Mobile',20000),
(103,'Headphones',3000),
(104,'Keyboard',1500);

-- orders
INSERT INTO orderss VALUES
(1001,1,'2025-01-10',53000),
(1002,2,'2025-01-15',20000),
(1003,1,'2025-02-05',1500),
(1004,3,'2025-02-20',23000),
(1005,5,'2025-03-01',50000);

-- order_items
INSERT INTO order_items VALUES
(1001,101,1),
(1001,103,1),
(1002,102,1),
(1003,104,1),
(1004,102,1),
(1004,103,1),
(1005,101,1);

-- TASK 1: CREATE INDEX

CREATE INDEX idx_orders_customer_id
ON orderss(customer_id);

PRINT 'Index created successfully';

-- TASK 2: ANALYZE QUERY

SET SHOWPLAN_TEXT ON;
GO

SELECT *
FROM orderss
WHERE customer_id = 1;
GO

SET SHOWPLAN_TEXT OFF;
GO

-- TASK 3: OPTIMIZED JOIN QUERY

SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orderss o
    ON c.customer_id = o.customer_id;

-- TASK 4: WHEN INDEX SHOULD NOT BE USED

SELECT *
FROM customers;

