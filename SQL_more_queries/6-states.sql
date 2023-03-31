-- creating a database and a table with not null values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
`id` INT UNIQUE NOT NULL,
`name` VARCHAR(256) NOT NULL
);
