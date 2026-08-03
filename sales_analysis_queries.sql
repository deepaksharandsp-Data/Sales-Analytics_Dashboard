USE sales_analytics;

SELECT *
FROM global_superstore
LIMIT 10;

SELECT COUNT(*) AS Total_Orders
FROM global_superstore;

SELECT ROUND(SUM(Profit), 2) AS Total_Profit
FROM global_superstore;

SELECT SUM(Quantity) AS Total_Quantity
FROM global_superstore;

SELECT Category,
ROUND(SUM(Sales), 2) AS Total_Sales
FROM global_superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT Category,
ROUND(SUM(Profit), 2) AS Total_Profit
FROM global_superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT Region,
ROUND(SUM(Sales), 2) AS Total_Sales
FROM global_superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT 'Customer Name',
ROUND(SUM(Sales), 2) AS Total_Sales
FROM global_superstore
GROUP BY 'Customer Name'
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT 'Product Name',
ROUND(SUM(Sales), 2) AS Total_sales
FROM global_superstore
GROUP BY 'Product Name'
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT Segment,
ROUND(SUM(Sales),2) AS Total_Sales
FROM global_superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;

SELECT Region,
ROUND(SUM(Profit),2) AS Total_Profit
FROM global_superstore
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT *
FROM global_superstore
WHERE Sales > 1000;

SELECT *
FROM global_superstore
WHERE Category = 'Furniture';

SELECT *
FROM global_superstore
WHERE Category = 'Technology'
ORDER BY Profit DESC;

SELECT Category,
ROUND(AVG(Sales), 2) AS Average_Profit
FROM global_superstore
GROUP BY Category;

SELECT Segment,
ROUND(AVG(Profit), 2) AS Average_Profit
FROM global_superstore
GROUP BY Segment;

SELECT 'Product Name',
ROUND(SUM(Profit), 2) AS Total_Profit
FROM global_superstore
GROUP BY 'Product Name'
ORDER BY Total_Profit DESC
LIMIT 10;

SELECT 'Product Name',
ROUND(SUM(Profit), 2) AS Total_Profit
FROM global_superstore
GROUP BY 'Product Name'
ORDER BY Total_Profit ASC
LIMIT 10;

SELECT 'Ship Mode',
COUNT(*) AS Total_Orders
FROM global_superstore
GROUP BY 'Ship Mode'
ORDER BY Total_orders DESC;

SELECT Category,
ROUND(SUM(Sales),2) AS Total_Sales
FROM global_superstore
GROUP BY Category
HAVING SUM(Sales) > 100000;

SELECT 'Order ID',
Profit,
CASE
WHEN Profit > 0 THEN 'Profit'
WHEN Profit < 0 THEN 'Loss'
ELSE 'Break Even'
END AS Profit_Status
FROM global_superstore;

SELECT Category,
COUNT(*) AS Total_Orders
FROM global_superstore
GROUP BY Category;

SELECT City,
ROUND(SUM(Sales),2) AS Total_Sales
FROM global_superstore
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 5;

SELECT State,
ROUND(SUM(Profit),2) AS Total_Profit
FROM global_superstore
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 5;

SELECT Country,
ROUND(SUM(Sales),2) AS Total_Sales
FROM global_superstore
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 5;

SELECT 'Customer Name',
ROUND(SUM(Profit),2) AS Total_Profit
FROM global_superstore
GROUP BY 'Customer Name'
ORDER BY Total_Profit DESC
LIMIT 5;

SELECT 'Order ID',
Discount,
Sales
FROM global_superstore
ORDER BY Discount DESC
LIMIT 10;

SELECT 'Order ID',
'Customer Name',
Sales
FROM global_superstore
ORDER BY Sales DESC
LIMIT 10;

