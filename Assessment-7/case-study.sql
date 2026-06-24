-- Create Database
CREATE DATABASE Ecommerces_DB;
GO

USE Ecommerces_DB;
GO

-- Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100)
);

-- Orders Table
CREATE TABLE orderss (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2)
);

-- Order Items Table
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orderss(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--Insert Sample Data

-- Customers
INSERT INTO customers VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Amit', 'Ahmedabad'),
(4, 'Neha', 'Surat'),
(5, 'Karan', 'Mumbai');

-- Products
INSERT INTO products VALUES
(101, 'Laptop', 50000),
(102, 'Mobile', 20000),
(103, 'Headphones', 3000),
(104, 'Keyboard', 1500);

-- Orders
INSERT INTO orderss VALUES
(1001, 1, '2025-01-10', 53000),
(1002, 2, '2025-01-15', 20000),
(1003, 1, '2025-02-05', 1500),
(1004, 3, '2025-02-20', 23000),
(1005, 5, '2025-03-01', 50000);

-- Order Items
INSERT INTO order_items VALUES
(1001, 101, 1),
(1001, 103, 1),
(1002, 102, 1),
(1003, 104, 1),
(1004, 102, 1),
(1004, 103, 1),
(1005, 101, 1);


--1. Total Orders Per Customer
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orderss o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC;

--2. Customers Who Never Placed an Order
SELECT
    c.customer_id,
    c.name,
    c.city
FROM customers c
LEFT JOIN orderss o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

--3. Highest Selling Product

SELECT TOP 1
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC;

--4. Monthly Sales Report

SELECT
    YEAR(order_date) AS sales_year,
    MONTH(order_date) AS sales_month,
    SUM(amount) AS total_sales
FROM orderss
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    sales_year,
    sales_month;

--5. Customers With Total Purchase Greater Than ₹50,000

SELECT
    c.customer_id,
    c.name,
    SUM(o.amount) AS total_purchase
FROM customers c
JOIN orderss o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000
ORDER BY total_purchase DESC;

--6. Top 3 Cities by Revenue

SELECT TOP 3
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orderss o
    ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;

