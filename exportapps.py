from __future__ import with_statement
import gzip
import shutil
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


def csv_export():
    s = "SELECT *"
    s += " FROM "
    s += "testapps"

    t_host = "localhost"
    t_port = "5432"
    t_dbname = "testdb"
    t_user = "postgres"
    t_pw = "Sulfi5687"
    db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
    db_cursor = db_conn.cursor()

    # Use the COPY function on the SQL we created above.
    sql_file_path = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(s)

    # Set up a variable to store our file path and name.
    t_path_n_file = "C:\\Users\\tempsubas\\apps.csv"

    # Trap errors for opening the file
    try:
        with open(t_path_n_file, 'w') as f_output:
            db_cursor.copy_expert(sql_file_path, f_output)
    except psycopg2.Error as e:
        return render_template("error.html", t_message=e)

    with open(t_path_n_file, 'rb') as f_in:
        with gzip.open('C:\\Users\\tempsubas\\apps.csv.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Success!

    # Clean up: Close the database cursor and connection
    db_cursor.close()
    db_conn.close()

    # Send the user on to some kind of informative screen.


if __name__ == "__main__":
    csv_export()