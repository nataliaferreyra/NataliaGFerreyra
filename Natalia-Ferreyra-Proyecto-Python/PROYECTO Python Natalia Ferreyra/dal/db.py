import sqlite3
from datetime import date
import hashlib

database = "super.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()
    
    @staticmethod
    def consultar(consulta, parametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            print(consulta)
            cursor.execute(consulta, parametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                                "UsuarioId"	INTEGER NOT NULL,
                                "Apellido"	VARCHAR(50),
                                "Nombre"	VARCHAR(30),
                                "FechaNacimiento"	VARCHAR(23),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(30),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(100),
                                "RolId"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "RolId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RolId")
                        );'''
        sql_productos = '''CREATE TABLE IF NOT EXISTS "Productos" (
                            "ProductoId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(20) NOT NULL UNIQUE,
                            "Descripcion"	VARCHAR(100) NOT NULL,
                            "Marca"	VARCHAR(20) NOT NULL,
                            "Categoria"	VARCHAR(20) NOT NULL,
                            "Cantidad"	INTEGER,
                            "Precio"	INTEGER,
                            "Activo" INTEGER NOT NULL DEFAULT 1,                         
                            PRIMARY KEY("ProductoId" AUTOINCREMENT)
                        );'''

        sql_carrito = '''CREATE TABLE IF NOT EXISTS "Carrito" (
                            "ProductoId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(20) NOT NULL UNIQUE,
                            "Descripcion"	VARCHAR(100) NOT NULL,
                            "Marca"	VARCHAR(20) NOT NULL,
                            "Categoria"	VARCHAR(20) NOT NULL,
                            "Cantidad"	INTEGER,
                            "Precio"	INTEGER,
                            "Activo" INTEGER NOT NULL DEFAULT 1,                         
                            PRIMARY KEY("ProductoId" AUTOINCREMENT)
                        );'''
        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles,"Productos": sql_productos, "Carrito": sql_carrito}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                cnn.commit()
            
    @staticmethod
    def poblar_tablasroles():        
        sql_roles = '''INSERT INTO Roles (RolId, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        tablas = {"Roles": sql_roles}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)
                    cnn.commit()
        
    @staticmethod
    def poblar_tablas():    

        sql_productos = '''INSERT INTO Productos (Nombre, Descripcion, Marca, Categoria, Cantidad, Precio) 
                    VALUES 
                        ("Leche","Leche entera 1lt","Cosalta","Lacteos", 50, 180),
                        ("Queso","Queso Cremoso 3kg","Cosalta","Lacteos", 30, 3500),
                        ("Manteca","Manteca 200g","Cosalta","Lacteos", 25, 360),
                        ("Dulce de Leche","Dulce de Leche Clasico 450g","Cosalta","Lacteos", 35, 450),
                        ("Fideos Tallarines","Tallarines Trigo 500g","Matarazzo","Pasta Seca", 100, 207),
                        ("Fideos Tirabuzones","Tirabuzones Trigo 500g","Matarazzo","Pasta Seca", 150, 190),
                        ("Fideos Cabello de Angel","Cabello de Angel Trigo 500g","Matarazzo","Pasta Seca", 200, 360);'''

        tablas = {"Productos": sql_productos}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    print(sql)
                    cursor.execute(sql)
                    cnn.commit()

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()