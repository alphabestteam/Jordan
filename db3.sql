1. UPDATE soldiers SET release_date = '2025-08-07' WHERE soldier_id = '8976148';

2. UPDATE soldiers SET base_id = (SELECT base_id FROM bases WHERE base_name = 'Camp Rabin') WHERE first_name = 'Noa';

3."To delete a row in a table that has foreign keys, you need to ensure that you maintain referential integrity in your database.
 This means that you need to handle the related rows in other tables" 
DELETE FROM soldiers WHERE soldier_id IN (SELECT city_id FROM soldiers WHERE city_id = 7);
 
4. SELECT c.city_name FROM cities c INNER JOIN students s ON c.city_id = s.city_id GROUP BY c.city_name ORDER BY(MAX((CURRENT_DATE - s.date_of_birth) / 365) > 17) DESC LIMIT 1;
5. 
SELECT c.city_name,
       COALESCE(s.student_count, 0) as student_counter,
       COALESCE(so.soldier_count, 0) as soldier_counter,
       COALESCE(s.student_count, 0) + COALESCE(so.soldier_count, 0) as total
FROM cities c
LEFT JOIN (SELECT city_id, COUNT(*) as student_count FROM students GROUP BY city_id) s ON c.city_id = s.city_id
LEFT JOIN (SELECT city_id, COUNT(*) as soldier_count FROM soldiers GROUP BY city_id) so ON c.city_id = so.city_id
ORDER BY c.city_name;


"A transaction in the context of a database is a sequence of one or more SQL statements that are executed as a single unit of work. the are used to ensure the integrity of data within a database.
 Either all the changes made by the transaction are applied, or none of them are. If any part of the transaction fails, the entire transaction is rolled back, and the database is left unchanged.
To add a transaction to a database, we need to use SQL statements. The basic structure of a transaction involves starting the transaction (begin) , performing one or more SQL operations and 
 committing the transaction or rolling it back based on the success or failure of the operations. An example: "
BEGIN; 
UPDATE soldiers SET city_id = 1 WHERE last_name = 'Smith';
UPDATE soldiers SET city_id = 2 WHERE last_name = 'Johnson';
COMMIT; 
