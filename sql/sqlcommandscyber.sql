SELECT *
FROM machines;

SELECT device_id, email_client
FROM machines;

SELECT device_id, operating_system, OS_patch_date
FROM machines;

SELECT event_id, country
FROM log_in_attempts;

SELECT username, login_date, login_time
FROM log_in_attempts;

SELECT *
FROM log_in_attempts;

SELECT *
FROM log_in_attempts
ORDER BY login_date;

SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;


SELECT * 
FROM machines;

SELECT * 
FROM machines 
INNER JOIN employees ON machines.device_id = employees.device_id;

SELECT * 
FROM machines 
LEFT JOIN employees ON machines.device_id = employees.device_id;

SELECT * 
FROM machines 
RIGHT JOIN employees ON machines.device_id = employees.device_id;

SELECT * 
FROM employees 
INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;

SELECT * 
FROM employees 
INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;