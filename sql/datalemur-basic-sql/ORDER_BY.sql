/*
SQL ORDER BY

Pharmacy Analytics (Part 1)
CVS Health SQL Interview Question
https://datalemur.com/questions/top-profitable-drugs

CVS Health is trying to better understand its pharmacy sales, and how well different products are selling. Each drug can only be produced by one manufacturer.

Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits. Display the result from the highest to the lowest total profit.

Definition:

cogs stands for Cost of Goods Sold which is the direct cost associated with producing the drug.
total_profit = Total Sales - Cost of Goods Sold

Note: you can substitute numbers for column names in the ORDER BY clause.
The numbers correspond to the columns you specify in the SELECT clause.
*/

SELECT drug, (total_sales - cogs) AS total_profit FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3;