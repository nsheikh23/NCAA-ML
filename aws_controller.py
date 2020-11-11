# Setting up Amazon RDS DB connection
rds_connection_string = "postgres:@localhost:5432/nabi"

# This function will return all rows from the table in the table requested
def get_all(table):
    return rds_connection_string.scan(
        TableName=table
        )