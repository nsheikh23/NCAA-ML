import psycopg2
import boto3

# Setting up Amazon RDS DB connection
conn = psycopg2.connect(
    host = "ncaa-athletics.cr5bt5kg46tf.us-west-1.rds.amazonaws.com",
    port = 5432,
    user = "postgres",
    password = "group1final",
    dbname = "NCAA_Athletics"
)


# This function will return all rows from the table in the table requested
def get_all(table):
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    details = cur.fetchall()
    return details