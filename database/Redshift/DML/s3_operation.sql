-- Unload Command
unload ('SELECT * FROM dw.daily_moods')
to 's3://health-analytics/data/Dataset/daily_moods.csv'
 PARALLEL FALSE --to a single file
 HEADER -- Keep Header
iam_role 'arn:aws:iam::123456789012:role/myRedshiftRole';


-- Copy Command
copy dw.daily_mood
from 's3://health-analytics/data/Dataset/daily_moods.csv'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
