import psycopg2
import pandas as pd


def sql_create_table():
    try:
        create_query = """CREATE TABLE class(
                FIRST_NAME VARCHAR(30),
                LAST_NAME VARCHAR(30),
                NUMBER NUMERIC(10),
                GENDER VARCHAR(1))"""

        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')

        print("Database successfully connected.")
        cur = connection.cursor()
        print("Cursor defined")
        cur.execute(create_query)
        print("Successfully created table.")

    except:
        print("Could not create table. Unknown error occurred")

    finally:
        if connection is not None:
            connection.commit()
            connection.close()

