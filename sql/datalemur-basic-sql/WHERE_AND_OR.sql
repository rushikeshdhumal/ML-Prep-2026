/*
SQL WHERE AND OR Practice Exercise
https://datalemur.com/questions/sql-where-and-or-practice-exercise

Filter Amazon reviews based on these two conditions:
1. the start count is greater than 2, and less than or equal to 4
2. the review must come from either user 123, 265, or 362
*/

SELECT * FROM reviews
WHERE (stars > 2 and stars <= 4) AND
(user_id = 123 OR user_id = 265 OR user_id = 362);