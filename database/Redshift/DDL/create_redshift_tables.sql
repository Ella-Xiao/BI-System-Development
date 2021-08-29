--https://www.obstkel.com/redshift-create-table-example
CREATE TABLE IF NOT EXISTS dw.daily_moods (
	user_id INTEGER NOT NULL
	,date TIMESTAMP NOT NULL
	,was_happy SMALLINT
	,created_at TIMESTAMP
	,updated_at TIMESTAMP)
distkey(user_id)
compound sortkey(user_id, date);
