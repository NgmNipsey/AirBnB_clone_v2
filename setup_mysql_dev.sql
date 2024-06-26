--a script that prepares a MySQL server for the project:
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--Create a new User:
CREATE USER IF NOT EXISTS 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--Granting privileges;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev_db'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev_db'@'localhost';
