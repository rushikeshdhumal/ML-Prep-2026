/*
SQL Math Practice Exercise: Big-Mover Months
https://datalemur.com/questions/sql-math-practice-exercise-big-mover-months

Display the stocks which had "big-mover months", and how many of those months they had. Order your results from the stocks with the most, to least, "big-mover months".

What is a big-mover month?
A "big-mover month" is when a stock closes up or down by greater than 10% compared to the price it opened at.

For example, when COVID hit and e-commerce became the new normal, Amazon stock in April 2020 had a big-mover month because the price shot up from $96.65 per share at open to $123.70 at close – a 28% increase!
*/

SELECT ticker, COUNT(ticker) FROM stock_prices
WHERE (close-open)/open > 0.10 OR (close-open)/open < -0.10
GROUP BY ticker
ORDER BY COUNT DESC;