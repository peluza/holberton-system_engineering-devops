-- Prepares a MySQL server for the project:
CHANGE MASTER TO MASTER_HOST = '35.190.152.71', MASTER_USER = 'replica_user', MASTER_PASSWORD = 'projectcorrection280hbtn', MASTER_LOG_FILE = 'mysql-bin.000001', MASTER_LOG_POS = 753;
FLUSH PRIVILEGES;