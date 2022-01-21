import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def  iniciarConexion(self):
        conexion=sqlite3.connect("sistema.s3db")
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSql = "SELECT * FROM contactos"
        cursor.execute(sentenciaSql)
        return cursor.fetchall()

    def crearContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSql = "INSERT INTO contactos (nombre, correo) VALUES(?,?)"
        cursor.execute(sentenciaSql,datosContacto)
        conexion.commit()
        conexion.close()

    def borrarContacto(self,idContacto):
        conexion=self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSql = "DELETE FROM contactos where id=(?)"
        cursor.execute(sentenciaSql,[idContacto])
        conexion.commit()
        conexion.close()

    def modificarContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSql = "UPDATE contactos SET nombre=?,correo=? WHERE id=?"
        cursor.execute(sentenciaSql,datosContacto)
        conexion.commit()
        conexion.close()