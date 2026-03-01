/*
SQL Tutorial Lesson: Superheroes' Likes
http://datalemur.com/questions/sql-case-marvel-avengers

Explore the Marvel Avengers dataset and write a query to categorize superheroes based on their average likes as follows:

Super Likes: Superheroes with an average likes count greater than or equal to 15,000.
Good Likes: Superheroes with an average likes count between 5,000 and 14,999 (inclusive).
Low Likes: Superheroes with an average likes count less than 5,000.
Display the actor and character's name, platform, average likes, and the corresponding likes category. Sort the results by average likes.
*/

SELECT actor,
character,
platform,
avg_likes,
CASE
  WHEN avg_likes >= 15000 THEN 'Super Likes'
  WHEN avg_likes BETWEEN 5000 AND 14999 THEN 'Good Likes'
  WHEN avg_likes < 5000 THEN 'Low Likes'
END AS likes_category
FROM marvel_avengers
ORDER BY avg_likes DESC;