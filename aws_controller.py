import psycopg2

# Setting up Amazon RDS DB connection
conn = psycopg2.connect(
    host = "ncaa-athletics.cr5bt5kg46tf.us-west-1.rds.amazonaws.com".host,
    port = "5432".port,
    user = "postgres".user,
    password = "group1final".password,
    db = "NCAA_Athletics".db
)


# This function will return all rows from the table in the table requested
def get_all(table):
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    details = cur.fetchall()
    return details