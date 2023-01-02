from dal.db import Db

def agregar(nombre, Descripcion , Marca , Categoria, Cantidad , Precio , producto_Id):    
    sql = "INSERT INTO Compras(Nombre, Descripcion, Marca, Categoria, Cantidad, Precio, ProductoId) VALUES(?, ?, ?, ?, ?, ?, ?);"
    parametros = (nombre, Descripcion , Marca , Categoria , Cantidad, Precio, producto_Id)
    Db.ejecutar(sql, parametros)

def actualizar(nombre, Descripcion , Marca , Categoria, Cantidad , Precio, producto_Id):    
    sql = "UPDATE Compras SET Nombre = ?, Descripcion = ?, Marca = ?, Categoria = ?, Cantidad = ?, Precio = ? WHERE ProductoId = ? AND Activo = 1;"
    parametros = (nombre, Descripcion , Marca , Categoria , Cantidad, Precio, producto_Id)
    Db.ejecutar(sql, parametros)    

def eliminar(producto_Id, logical = True):    
    if logical:
        sql = "UPDATE Productos SET Activo = 0 WHERE ProductoId = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Productos WHERE ProductoId = ?;"
    parametros = (producto_Id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT * FROM Productos;'''
    result = Db.consultar(sql)
    return result

def filtrar(producto):    
    sql = '''SELECT p.ProductoId, p.Nombre, p.Descripcion, p.Marca, p.Categoria, p.Cantidad, p.Precio
            FROM Productos p
            WHERE p.Producto LIKE ? AND p.Activo = 1 ;'''
    parametros = ('%{}%'.format(producto),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(producto):    
    sql = "SELECT Producto FROM Productos WHERE Producto = ? AND Activo = 1;"
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(producto):
    sql = "SELECT COUNT(*) FROM Productos WHERE Nombre = ? AND Activo = 1;"
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT p.ProductoId, p.Nombre, p.Descripcion, p.Marca, p.Categoria, p.Cantidad, p.Precio
            FROM Productos p
            WHERE p.ProductoId = ? AND p.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def obtener_nombre_producto(producto):
    sql = '''SELECT p.ProductoId, p.Nombre, p.Descripcion, p.Marca, p.Categoria, p.Cantidad, p.Precio     
            FROM Productos p
            WHERE p.ProductoId = ? AND p.Activo = 1;'''
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)    
    return result