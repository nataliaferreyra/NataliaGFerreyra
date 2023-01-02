import tkinter as tk
import tkinter.font as tkFont
from frmusers import Users
from dal.db import Db
from frmselectprod import Productos
from frmclients import Compras

class Dashboardclientes(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Principal")        
        width=548
        height=100
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_996=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#333333"
        GLabel_996["justify"] = "left"
        GLabel_996["text"] = ""
        GLabel_996.place(x=10,y=10,width=120,height=30)

        GButton_196=tk.Button(self)
        GButton_196["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_196["font"] = ft
        GButton_196["fg"] = "#000000"
        GButton_196["justify"] = "center"
        GButton_196["text"] = "Realizar una compra"
        GButton_196.place(x=190,y=40,width=165,height=35)
        GButton_196["command"] = self.abrir_productos


    def abrir_productos(self):
        Compras(self)

    def abrir_carrito(self):
        print("carrito")

    def abrir_factura(self):
        print("factura")