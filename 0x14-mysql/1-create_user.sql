-- Prepares a MySQL server for the project:
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost';
SET PASSWORD FOR 'holberton_user'@'localhost' = PASSWORD('projectcorrection280hbtn');
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
