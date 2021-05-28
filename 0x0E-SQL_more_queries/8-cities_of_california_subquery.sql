-- List of cities in California in cities table
-- Referencing state table in database
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC; 
