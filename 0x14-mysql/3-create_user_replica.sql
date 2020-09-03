-- Prepares a MySQL server for the project:
CREATE USER IF NOT EXISTS 'replica_user'@'%';
SET PASSWORD FOR 'replica_user'@'%' = PASSWORD('projectcorrection280hbtn');
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
