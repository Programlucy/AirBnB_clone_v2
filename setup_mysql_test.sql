-- Script that prepares a server
-- 
-- Creates hbnb_dev_db database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates user hbnb_dev if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

--
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

