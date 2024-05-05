CREATE TABLE TrainingDB.sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    region VARCHAR(50),
    product VARCHAR(50),
    sale_date DATE,
    amount DECIMAL(10, 2)
);
-- @block
INSERT INTO TrainingDB.sales (region, product, sale_date, amount)
VALUES
    ('North', 'Product A', '2024-01-01', 100),
    ('North', 'Product B', '2024-01-01', 200),
    ('North', 'Product A', '2024-01-02', 150),
    ('North', 'Product B', '2024-01-02', 250),
    ('South', 'Product A', '2024-01-03', 120),
    ('South', 'Product B', '2024-01-01', 180),
    ('South', 'Product A', '2024-01-04', 130),
    ('South', 'Product B', '2024-01-02', 220);

-- @block
DROP TABLE TrainingDB.sales
-- @block
SELECT 
    sales.product,
    sales.sale_date,
    SUM(amount) OVER (PARTITION BY sales.product ORDER BY sale_date) as test
FROM 
    TrainingDB.sales;

-- @block
SELECT
    DISTINCT sales.region,
    sales.product,
    SUM(amount) OVER (PARTITION BY sales.region, sales.product ORDER BY sales.product) as Sales_by_Reagion
FROM
    TrainingDB.sales;

SELECT
    DISTINCT sales.region,
    SUM(amount) OVER (PARTITION BY sales.region) as Sales_by_Reagion
FROM
    TrainingDB.sales;