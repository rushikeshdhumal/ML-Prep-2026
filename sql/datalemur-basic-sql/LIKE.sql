/*
SQL LIKE %
https://datalemur.com/questions/sql-like-practice-exercise-1

You have a table of 1000 customer records from a small-business based in Australia.

Find all customers whose first name starts with "F" and the last letter in their last name is "ck".

*/

SELECT * FROM customers
WHERE customer_name LIKE 'F%'
AND
customer_name LIKE '%ck';

/*
SQL LIKE _
https://datalemur.com/questions/sql-like-_-practice-exercise

You have a table of 1000 customer records from a small-business based in Australia.

Find all customers where the 2nd and 3rd letter in their name is "e".
*/

SELECT * FROM customers
WHERE customer_name LIKE '_ee%';