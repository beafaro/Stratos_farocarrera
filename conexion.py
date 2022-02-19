import os
import sqlite3

import xlwt as xlwt
from PyQt5 import QtSql
from PyQt5.uic.properties import QtGui, QtWidgets


class Conexion():
    def create_DB(filename):

        try:
            con = sqlite3.connect(database=filename)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS puntuaciones (id INTEGER NOT NULL, nombre TEXT NOT NULL, puntuacion INTEGER NOT NULL, PRIMARY KEY(id AUTOINCREMENT))")
            con.commit()
            con.close()

            ''' creacion de directorios '''
            if not os.path.exists('.\\puntuaciones'):
                os.mkdir('.\\puntuaciones')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("error")
            msg.exec()

    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, "No se puede abrir la base de datos.\n" "Haz click para continuar",
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print("Conexión establecida")
                return True
        except Exception as error:
            print("Problemas en conexión ", error)


    '''
    Módulos gestión base datos cliente
    '''
    def guardarPuntuacion(puntuacion):
        """

        Módulo que recibe datos de un cliente y los carga en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO puntuaciones (nombre, puntuacion) '
                'VALUES (:nombre, :puntuacion)')
            query.bindValue(":nombre", str(puntuacion[0]))
            query.bindValue(":puntuacion", str(puntuacion[1]))

            if not query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas al realizar el guardado ", error)

    def cargarPuntuaciones(self):

        resultados = []

        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT nombre, puntuacion FROM puntuaciones order by puntuacion desc")
            if query.exec_():
                numRows = 0
                while query.next() and numRows < 5:
                    row = []
                    row.append(query.value(0))
                    row.append(str(query.value(1)))
                    resultados.append(row)
                    numRows += 1
        except Exception as error:
            print("Problemas obtener puntuaciones ", error)

        return resultados