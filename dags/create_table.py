# import pandas
import psycopg2


def sql_create_table():

        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        add_data = 'create table IF NOT EXISTS docker_sahil_table as select dag_id, execution_date from dag_run; '
        cursor.execute(add_data)
        conn.commit()

        print("data added to a new table Successfully")
