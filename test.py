import psycopg2

try:
    connection = psycopg2.connect(
        user='edu_user',
        password='edungwo1',
        host="127.0.0.1",
        port="5432",
        database="analysis"
    )

    cursor = connection.cursor()

    # Retrieve from an existing table

    result = cursor.execute("SELECT id, first_name,last_name, school from teachers ;")
    record = cursor.fetchmany(3)
    print(record)
    print("Connection successful")

    # create a table
    create_table_query = \
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """

    insert_users_query = \
        """
    INSERT INTO vendors( vendor_name)
    VALUES('John Eze');
    """
    cursor.execute(create_table_query)
    print("Table created successfully in Postgres")
    cursor.execute(insert_users_query)
    connection.commit()
except Exception as e:
    print(e)
