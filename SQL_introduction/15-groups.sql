-- listing the number of records with the same socre in the table
SELECT score, COUNT (*) AS number
GROUP BY score
ORDER BY score DESC;
