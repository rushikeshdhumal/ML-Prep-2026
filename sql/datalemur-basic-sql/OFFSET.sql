/*
SQL OFFSET clause is used to specify the number of rows to skip before starting to return rows from the query.
It is often used in conjunction with the LIMIT clause to paginate results.

The following query skips the first 10 phone calls and fetches the subsequent 5 phone calls received.
This means that we're disregarding the first 10 rows of the sorted result, effectively starting our
selection from the 11th row onwards.
*/

SELECT * 
FROM callers
ORDER BY call_received DESC
OFFSET 10
LIMIT 5;