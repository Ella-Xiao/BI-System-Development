-- Export MySQL Data to Amazon S3
SELECT * FROM TABLE
INTO OUTFILE S3 's3://some-bucket-name/users'
FILELDS TERMINATED BY ','
ENCLOSED by '"'
LINES TERMINATED BY '\n'


LOAD DATA FROM S3 PREFIX 's3://some-bucket-name/users'
INTO TABLE users;
