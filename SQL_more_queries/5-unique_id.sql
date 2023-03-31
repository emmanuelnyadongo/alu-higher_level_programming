-- creating a table with a default value stated and also it should be unique
CREATE TABLE IF NOT EXISTS unique_id(
`id` INT  UNIQUE DEFAULT 1,
`name` VARCHAR(256)
);
