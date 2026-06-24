USE ECommerces_db;

-- Tasks :

--  1.Add index to improve search on orders.customer_id 
CREATE INDEX idx_customer_id
ON orders(customer_id);

EXEC sp_helpindex 'orders';

--  2.Use EXPLAN to analyze query
SET SHOWPLAN_ALL ON;
SELECT * FROM orders
WHERE customer_id = 1;
SET SHOWPLAN_ALL OFF;

--  3.Optimize a slow join query
SELECT c.name,
o.order_id,
o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

--  4.Explain when index should not be used

SELECT *
FROM customers;



