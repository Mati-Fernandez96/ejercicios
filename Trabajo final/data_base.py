import sqlite3 as sql
import os

abs_file_path = "dataBase/padron.db"

def crearBaseDatos():
    conn = sql.connect(abs_file_path) 
    conn.commit()
    conn.close()

def crearTabla():
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE padron (
            Apellido text,
            Nombre text,
            DNI integer,
            voto integer
        )"""
    )
    conn.commit()
    conn.close()

def insertarFila(apellido, nombre, dni, voto = 0):
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO padron VALUES ('{apellido}', '{nombre}', {dni}, {voto})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def leerFilas():
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM padron"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    #print(datos)

def insertarFilas(listaVotantes):
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO padron VALUES (?, ?, ?, ?)"
    cursor.executemany(instruccion, listaVotantes)
    conn.commit()
    conn.close()

def buscar(condicion):
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM padron WHERE {condicion}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos   


def actualizarCampos(qActualizar,qCampo,aQuien):
    conn = sql.connect(abs_file_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE padron SET {qActualizar} WHERE {qCampo} like {aQuien}"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()
    
"""
if __name__ == "__main__":
    #crearBaseDatos()
    #crearTabla()
    #leerFilas()
    listaVontantes = [
        ("Gonzales", "Juan", 32536432, 0),
        ("Lopez", "Gregorio", 36353657, 0),
        ("Gomez", "Franco", 87654321, 1),
        ("Ruarte", "Ana", 40876345, 0),
        ("Romero", "Carlos", 12345678, 1)
    ]
    #insertarFilas(listaVontantes)


    quien = "40876345"
    actualizar = "voto = 1"
    campo = "DNI"
    actualizarCampos(actualizar,campo,quien)



    filtroNoVoto = "voto = 0"
    buscar(filtroNoVoto)

    filtroVoto = "voto = 1"
    buscar(filtroVoto)


    pass
    



crearBaseDatos()
crearTabla()
listaVontantes = [
        ("Gonzales", "Juan", 32536432, 0),
        ("Lopez", "Gregorio", 36353657, 0),
        ("Gomez", "Franco", 87654321, 1),
        ("Ruarte", "Ana", 40876345, 0),
        ("Romero", "Carlos", 12345678, 1)
]
insertarFilas(listaVontantes)
"""


def checkVoto (dniVotante):
    validar = False
    listaVotantes = leerFilas()
    for _ in listaVotantes:
        if dniVotante == _[2] and _[3] == 1:
            validar = True
    return validar        

