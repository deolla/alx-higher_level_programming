-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');
SELECT * FROM cities
WHERE state_id = @california_state_id
ORDER BY id ASC;
