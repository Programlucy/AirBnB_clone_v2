-- Script that prepares a server
-- 
-- Creates hbnb_dev_db database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates user hbnb_dev if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

