# https://blog.panoply.io/how-to-move-your-mysql-to-amazon-redshift


# Export MySQL Data to Amazon S3
export_query = """
                SELECT * FROM TABLE
                INTO OUTFILE '/tmp/daily_overall.csv'
                FILELDS TERMINATED BY ','
                ENCLOSED by '"'
                LINES TERMINATED BY '\n'
                """
