1. SELECT s.soldier_id, s.first_name, s.last_name FROM soldiers s JOIN bases b ON s.base_id = b.base_id WHERE b.base_name = 'Bahad 4';

2. SELECT first_name, last_name,  EXTRACT(YEAR FROM age(release_date, enlistment_date)) AS service_years FROM soldiers ORDER BY service_years DESC LIMIT 1;

3. SELECT c.city_name, COUNT(*) AS soldiers_exceeded_release_date FROM soldiers s JOIN cities c ON s.city_id = c.city_id WHERE s.release_date < CURRENT_DATE GROUP BY c.city_name;

4. SELECT * FROM soldiers s JOIN bases b ON s.base_id = b.base_id WHERE s.enlistment_date > '2000-01-01' AND LOWER(b.base_name) LIKE '%naval%';

5. SELECT t.id, t.first_name, t.school_name, t.major_name, c.city_name FROM (SELECT s.id, s.first_name, sch.school_name, m.major_name, s.city_id FROM students s JOIN schools sch ON s.school_id = sch.school_id JOIN majors m ON s.major_id = m.major_id WHERE RIGHT(s.id, 1) = '9') AS t JOIN cities c ON t.city_id = c.city_id ORDER BY c.city_name;

6. SELECT s.first_name, s.last_name, s.city_id FROM students s JOIN majors m ON s.major_id = m.major_id WHERE (m.major_name = 'Business' OR m.major_name = 'Economics') AND s.city_id IN ( SELECT city_id FROM soldiers WHERE first_name LIKE 'M%' OR last_name LIKE 'M%');

