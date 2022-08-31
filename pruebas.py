from tkinter import *
import mysql.connector
from PyQt5 import QtWidgets,uic
from lectura_bd import mov

raiz=Tk()

raiz.title("ERP CLASE")

raiz.resizable(1,1)#Tamaño ventana width/heigth

#raiz.iconbitmap("gato.ico")#cambio icono archivo con extension .ico  conversor.ico 

raiz.geometry("650x350")#tamaño ventana por defecto

raiz.config(bg="green")

lblTablaMovimientos=Label(raiz,text="Tabla Movimientos",font=('bold',30))
lblTablaMovimientos.place(x=20,y=30)
lblTablaMovimientos.pack()

q="Select * from movimientos"

conexion=mov()

todo,cursor=conexion.select_all()



lblSQL=Label(raiz,text=todo,font=('bold',10))
lblSQL.place(x=20,y=60)
lblSQL.pack()

raiz.mainloop()#Siempre ultimo