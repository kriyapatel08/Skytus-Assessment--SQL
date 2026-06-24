# E-Commerce Database Analysis

## Project Overview
This project demonstrates the use of Python and SQL to analyze data from an E-Commerce Database.

## Database Schema

### customers
- customer_id
- name
- city

### orders
- order_id
- customer_id
- order_date
- amount

### products
- product_id
- product_name
- price

### order_items
- order_id
- product_id
- quantity

## Tasks Implemented

1. Total Orders Per Customer
2. Customers Who Never Placed an Order
3. Highest Selling Product
4. Monthly Sales Report
5. Customers with Total Purchase Greater Than ₹50,000
6. Top 3 Cities by Revenue

## Technologies Used

- Python 3
- SQLite
- SQL Queries

## How to Run

1. Install Python 3.
2. Save the file as `ecommerce_analysis.py`.
3. Open terminal or command prompt.
4. Run:

```bash
python ecommerce_analysis.py