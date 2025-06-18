#Notboring movies 
sql leetcode 

SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1       -- Select rows with odd-numbered ID
  AND description != 'boring'  -- Filter out 'boring' descriptions
ORDER BY rating DESC;      -- Sort by rating in descending orde
