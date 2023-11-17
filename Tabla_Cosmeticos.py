import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("Cosmeticos.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE Articulo(Folio INTEGER PRIMARY KEY, Precio FLOAT NOT NULL, Descripcion TEXT NOT NULL, Fecha TIMESTAMP NOT NULL);")
        print("Tabla exitosamente creada")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    if(conn):
        conn.close()
