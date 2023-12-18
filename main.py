import pandas as pd
import pyodbc as pdb
import psycopg2
import numpy as np

# CONECTARSE DATAFRAME

host = "localhost"
database = "postgres"
user = "root"
password = "root"
port = "5432"

connection_target = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )

# Cursor
cur_target = connection_target.cursor()