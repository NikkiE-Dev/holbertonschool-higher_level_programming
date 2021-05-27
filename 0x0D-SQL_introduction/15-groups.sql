-- List record in Descending order
SELECT `score`, COUNT(`score`) as 'number' FROM second_table GROUP BY `score` ORDER BY COUNT(`score`) DESC;