-- Lists all records in "second_table" with a score that's >= 10
-- Records are ordered by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
