import psycopg2
from config import config


def create_tables():
    commands = (
        """
        CREATE TABLE user (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE action (
                action_id SERIAL PRIMARY KEY,
                action_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE user_actions (
                user_id INTEGER NOT NULL,
                action_id INTEGER NOT NULL,
                PRIMARY KEY (user_id , action_id),
                FOREIGN KEY (user_id)
                    REFERENCES vendors (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (action_id)
                    REFERENCES parts (action_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 'Tables failed'
    finally:
        if conn is not None:
            conn.close()
        return 'Tables Created'
    return 'Tables unknown status'

