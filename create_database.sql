CREATE DATABASE khaonewsdb CHARACTER SET utf8;
CREATE USER 'khaonewsdb'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON khaonewsdb.* TO 'khaonewsdb'@'localhost';
SET GLOBAL transaction_isolation = 'READ-COMMITTED';