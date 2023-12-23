#archivo para poner los filtros

import pandas as pd
import pyodbc as pdb
import psycopg2
import numpy as np
import faker

#CONEXIONES BASE DE DATOS
host = "localhost" #SI ES PARA EL DOCKER-COMPOSE, CAMBIAR POR "postgres"
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