import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    queries = (
        """
        CREATE TABLE vendors2 (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:

        # connect to the PostgreSQL server: change to your db details

        conn = psycopg2.connect(
            user='edu_user',
            password='edungwo1',
            host="127.0.0.1",
            port="5432",
            database="analysis"
        )
        cur = conn.cursor()
        # create table one by one
        for query in queries:
            cur.execute(query)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Run the script.
if __name__ == '__main__':
    create_tables()
