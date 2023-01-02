import sqlite3
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
from frmsprod import Producto
import bll.productos as product


class Productos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.select_id = -1
        self.title("Listado de Productos")
        width = 1000
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464 = Label(self)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Productos:"
        GLabel_464.place(x=10, y=10, width=70, height=25)

        self.tv = ttk.Treeview(
            self,
            columns=("col1", "col2", "col3", "col4", "col5", "col6"),
            name="tvProductos",
        )
        self.tv.column("#0", width=78)
        self.tv.column("col1", width=100, anchor=CENTER)
        self.tv.column("col2", width=150, anchor=CENTER)
        self.tv.column("col3", width=150, anchor=CENTER)
        self.tv.column("col4", width=150, anchor=CENTER)
        self.tv.column("col5", width=120, anchor=CENTER)
        self.tv.column("col6", width=120, anchor=CENTER)

        self.tv.heading("#0", text="ProductoId", anchor=CENTER)
        self.tv.heading("col1", text="Nombre", anchor=CENTER)
        self.tv.heading("col2", text="Descripcion", anchor=CENTER)
        self.tv.heading("col3", text="Marca", anchor=CENTER)
        self.tv.heading("col4", text="Categoria", anchor=CENTER)
        self.tv.heading("col5", text="Cantidad", anchor=CENTER)
        self.tv.heading("col6", text="Precio", anchor=CENTER)
        self.tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tv.place(x=30, y=70, width=900, height=300)

        nombre_db = "super.db"
        conexion = sqlite3.connect(nombre_db)
        cursor = conexion.cursor()
        sql = "SELECT * FROM Productos;"
        cursor.execute(sql)
        datos = cursor.fetchall()

        self.refrescar()

        ft = tkFont.Font(family="Times", size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=530, y=10, width=70, height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=610, y=10, width=70, height=25)
        btn_editar["command"] = self.editar

        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=690, y=10, width=70, height=25)
        btn_eliminar["command"] = self.eliminar

    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Producto(self, True)

    def editar(self):
        Producto(self, True, self.select_id)

    def eliminar(self):
        answer = tkMsgBox.askokcancel(
            self.master.master.title(), "¿Está seguro de eliminar este registro?"
        )
        if answer:
            product.eliminar(self.select_id, False)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):
        tvProductos = self.nametowidget("tvProductos")
        for record in tvProductos.get_children():
            tvProductos.delete(record)
        registro = product.listar()
        for producto in registro:
            tvProductos.insert(
                "",
                END,
                text=producto[0],
                values=(
                    producto[1],
                    producto[2],
                    producto[3],
                    producto[4],
                    producto[5],
                    producto[6],
                ),
            )
