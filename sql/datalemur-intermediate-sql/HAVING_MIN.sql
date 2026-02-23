/*
SQL HAVING MIN
https://datalemur.com/questions/sql-having-min-practice-exercise

As aggregate functions are not allowed in WHERE clause,
we can use HAVING clause to filter the records after
grouping them.

Use SQL's HAVING & MIN commands to find all FAANG stocks whose open share price was always greater than $100.
*/

SELECT ticker, MIN(open) FROM stock_prices
GROUP BY ticker
HAVING MIN(open) > 100;