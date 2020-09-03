-- Prepares a MySQL server for the project:
CREATE USER IF NOT EXISTS 'replica_user'@'localhost';
SET PASSWORD FOR 'replica_user'@'localhost' = PASSWORD('projectcorrection280hbtn');
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'localhost';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
