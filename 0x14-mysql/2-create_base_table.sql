-- Prepares a MySQL server for the project:
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (ID INT, name VARCHAR(256));
INSERT INTO nexus6 (ID, name) VALUES (1, "Leon");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
