import pandas as pd
import datetime
import csv
import sys
import os.path

import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect('Tabla_Cosmeticos.db') as conn:
        print(sqlite3.version)
except Error as e:
        print(e)

venta = dict() # Diccionario principal
codigo = 0 # Claves autoincrementables

if os.path.exists("Productos.csv") == True:
        productos = pd.read_csv("Productos.csv", index_col=0)
        print(f"Folio {codigo}")
        print()
else:
    product_dict = {'Articulo':['Labial', 'Rimel', 'Sombras', 'Corrector', 'Esmalte de uñas', 'Delineador', 'Cejas'],
                    'Precio':[60,80,40,60,50,20,30],
                    'Descripcion':['Mate sin resecar labios','Pestañas largas','Diferentes colores','Con Glitter','No te saca arrugas','Delineadores mate','Solo colores cafes']}
    productos  = pd.DataFrame(product_dict)

if os.path.exists("Ventas.csv") == True:
    ventas = pd.read_csv("Ventas.csv", index_col=0)
else:
    ventas = pd.DataFrame(columns=["Fecha", "Folio", "Cantidad", "Pago total"])

while True: # Ciclo para hacer menús
    print("1.- Añadir una nueva venta \n2.- Consultar una venta \n3.- Salir")
    opcion = int(input("Elige la opcion deseada: "))
    print()
    print("-------------")
    if opcion  ==1:
        precio_total = 0

        try:
            with sqlite3.connect("Tabla_Cosmeticos.db") as conn:
                print("Conexión establecida")
                mi_cursor = conn.cursor()
                Fecha = input("Dime la fecha (dd/mm/aaaa): ")
                fecha_con = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                fecha_2 = datetime.datetime.combine(fecha_con, datetime.datetime.min.time())

                while opcion == 1:
                print(productos['Articulo'])

                Folio = int(input("Dime un folio: "))
                num = int(input("Numero \n>"))
                venta_cantidad = int(input("Cantidad \n>"))
                precio_total += productos.iloc[num,1] * venta_cantidad
                ventas = ventas.append({'Cantidad':venta_cantidad, 'Pago total':precio_total}, ignore_index=True)
                print(f'Precio total a pagar: {precio_total}')
                print("El articulo se añadio exitosamente")
                mi_cursor.execute("INSERT INTO ARTICULO VALUES(:folio,:descripcion ,:precio,:fecha);", ventas)
                opcion = int(input("Desea agregar otro producto? 1.Si 2.No \n>"))
                print('-----------')

        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()

     elif opcion == 2:
        try:
            with sqlite3.connect("Tabla_Cosmeticos.db") as conn:
                mi_cursor = conn.cursor()

                busca_fecha_capturada = int(input("Que fecha dese consultar? Ejemplo 01/05/2021 \n>"))
                registro = mi_cursor.fetchall()
                if registro:
                    for Folio, Precio, Decripcion, Fecha in registro:
                        print(articulo)
                    else:
                        print("-- ERROR --")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()

    elif opcion == 3:
        print("EJECUCION FINALIZADA")
        break