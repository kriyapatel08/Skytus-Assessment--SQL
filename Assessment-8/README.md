# SQL Assessment - Database Optimization

## Overview

This project demonstrates database optimization techniques using SQL Server. The assessment includes creating indexes, analyzing query execution plans, optimizing JOIN operations, and understanding when indexes should not be used.

---

## Database Used

**Database Name:** ecommerce_db

### Tables

1. customers
2. orders
3. products
4. order_items

---

## Task 1: Create an Index

### Objective

Improve query performance by creating an index on the `customer_id` column of the `orders` table.

### Query

```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

### Result

The index helps SQL Server locate records faster when filtering or joining using `customer_id`.

---

## Task 2: Analyze Query Performance

### Objective

Analyze how SQL Server executes a query.

### Query

```sql
SET SHOWPLAN_TEXT ON;
GO

SELECT *
FROM orders
WHERE customer_id = 1;
GO

SET SHOWPLAN_TEXT OFF;
GO
```

### Result

Execution plans show whether SQL Server performs a Table Scan or Index Seek.

---

## Task 3: Optimize a Slow JOIN Query

### Query

```sql
SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;
```

### Optimization

Creating an index on `orders(customer_id)` improves JOIN performance by reducing search time.

### Result

The query executes faster using an Index Seek instead of scanning the entire table.

---

## Task 4: Explain When Index Should Not Be Used

### Example Query

```sql
SELECT *
FROM customers;
```

### Situations Where Indexes Should Not Be Used

1. Small tables where a full table scan is faster.
2. Columns with low cardinality (few unique values).
3. Tables with frequent INSERT, UPDATE, or DELETE operations.
4. Columns rarely used in WHERE, JOIN, ORDER BY, or GROUP BY clauses.
5. When too many indexes already exist, causing maintenance overhead.

### Result

Indexes improve read performance but may reduce write performance and increase storage requirements.

---

## Conclusion

This assessment demonstrates:

* Creating and using indexes.
* Query execution analysis.
* JOIN optimization techniques.
* Best practices for index usage.

These techniques help improve database performance and efficiency in real-world applications.

```
```
