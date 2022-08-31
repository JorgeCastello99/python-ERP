# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from lectura_bd import mov


class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        
        self.campos=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(935, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(115, 210, 22), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 50, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 90, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 170, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.edtId = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtId.setGeometry(QtCore.QRect(110, 50, 250, 30))
        self.edtId.setObjectName("edtId")
        self.edtId.setReadOnly(True)
        self.edtObservaciones = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtObservaciones.setGeometry(QtCore.QRect(530, 130, 371, 121))
        self.edtObservaciones.setObjectName("edtObservaciones")
        self.edtObservaciones.setReadOnly(True)
        self.edtPrecio = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtPrecio.setGeometry(QtCore.QRect(110, 210, 250, 30))
        self.edtPrecio.setObjectName("edtPrecio")
        self.edtPrecio.setReadOnly(True)
        self.edtCantidad = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtCantidad.setGeometry(QtCore.QRect(110, 170, 250, 30))
        self.edtCantidad.setPlainText("")
        self.edtCantidad.setObjectName("edtCantidad")
        self.edtCantidad.setReadOnly(True)
        self.edtProveedor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtProveedor.setGeometry(QtCore.QRect(530, 80, 371, 30))
        self.edtProveedor.setObjectName("edtProveedor")
        self.edtProveedor.setReadOnly(True)
        self.edtProducto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtProducto.setGeometry(QtCore.QRect(110, 130, 250, 30))
        self.edtProducto.setObjectName("edtProducto")
        self.edtProducto.setReadOnly(True)
        self.edtFactura = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtFactura.setGeometry(QtCore.QRect(110, 90, 250, 31))
        self.edtFactura.setObjectName("edtFactura")
        self.edtFactura.setReadOnly(True)
        self.edtCliente = QtWidgets.QTextEdit(self.centralwidget)
        self.edtCliente.setGeometry(QtCore.QRect(530, 40, 371, 30))
        self.edtCliente.setObjectName("edtCliente")
        self.edtCliente.setReadOnly(True)
        self.edtBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.edtBuscar.setGeometry(QtCore.QRect(420, 10, 211, 21))
        self.edtBuscar.setObjectName("edtBuscar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 10, 81, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.tableMovs = QtWidgets.QTableWidget(self.centralwidget)
        self.tableMovs.setGeometry(QtCore.QRect(0, 270, 881, 321))
        self.tableMovs.setColumnCount(8)
        self.tableMovs.setObjectName("tableMovs")


      

        #self.tableMovs.setRowCount(0)

    
        self.tableMovs.setHorizontalHeaderLabels(["id","Factura","Producto","Cantidad","Precio","Cliente","Proveedor","Observaciones"])
        self.lineas2=self.select_Todo()


        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableMovs.horizontalHeader().setDefaultSectionSize(110)
        self.tableMovs.horizontalHeader().setMinimumSectionSize(60)

        

        self.btnBuscar = QtWidgets.QToolButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(645, 10, 21, 21))
        self.btnBuscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ruta/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnBuscar.clicked.connect(self.buscamospor)
        self.cbbBuscarpor = QtWidgets.QComboBox(self.centralwidget)
        self.cbbBuscarpor.setGeometry(QtCore.QRect(270, 10, 131, 21))
        self.cbbBuscarpor.setObjectName("cbbBuscarpor")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.cbbBuscarpor.addItem("")
        self.btnAdelante = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdelante.setGeometry(QtCore.QRect(80, 10, 21, 25))
        self.btnAdelante.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ruta/flecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdelante.setIcon(icon1)
        self.btnAdelante.setObjectName("btnAdelante")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(40, 10, 21, 25))
        self.btnAtras.setText("")

        self.btnAtras.clicked.connect(self.onClickFlechaAt)
        self.btnAdelante.clicked.connect(self.onClickFlechaAd)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ruta/espalda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAtras.setIcon(icon2)
        self.btnAtras.setObjectName("btnAtras")
        MainWindow.setCentralWidget(self.centralwidget)


        self.btnTodo = QtWidgets.QPushButton(self.centralwidget)
        self.btnTodo.setGeometry(QtCore.QRect(745, 10, 80, 21))
        self.btnTodo.setText("Ver todo")
        self.btnTodo.setObjectName("btnTodo")
        self.btnTodo.clicked.connect(self.onClickTodo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def rellenaVisual(self):
        bucle=0
        while bucle < 8:
            if bucle==0:
                self.edtId.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==1:
                self.edtFactura.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==2:
                self.edtProducto.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==3:
                self.edtCantidad.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==4:
                self.edtPrecio.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==5:
                self.edtCliente.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==6:
                self.edtProveedor.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            elif bucle==7:
                self.edtObservaciones.setPlainText(self.tableMovs.item(self.campos, bucle).text())
            bucle = bucle + 1
            
        
    def select_Todo(self):
        conexion=mov()
        datos,cursor=conexion.select_all()
        self.tableMovs.setRowCount(cursor.rowcount)
        lineas1=cursor.rowcount

        if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

        else:
            return 0

    def select_WProducto(self,producto):
        conexion=mov()
        datos,cursor=conexion.select_wproducto(producto)
        self.tableMovs.setRowCount(cursor.rowcount)
        lineas1=cursor.rowcount

        if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

        else:
            return 0
        
    def buscamospor(self): 
        item=self.cbbBuscarpor.currentText()
        if(item=="Id"):
            conexion=mov()
            datos,cursor=conexion.select_wid(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0

        if(item=="Factura"):
            conexion=mov()
            datos,cursor=conexion.select_wfactura(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0

        if(item=="Producto"):
            conexion=mov()
            datos,cursor=conexion.select_wproducto(float(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0   
        
        if(item=="Cantidad"):
            conexion=mov()
            datos,cursor=conexion.select_wcantidad(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            
            lineas1=cursor.rowcount
            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0
   
        
        if(item=="Precio"):
            conexion=mov()
            datos,cursor=conexion.select_wprecio(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0
        
        if(item=="Cliente"):
            conexion=mov()
            datos,cursor=conexion.select_wcliente(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0
        
        if(item=="Proveedor"):
            conexion=mov()
            datos,cursor=conexion.select_wproveedor(int(str(self.edtBuscar.toPlainText())))
            self.tableMovs.setRowCount(cursor.rowcount)
            lineas1=cursor.rowcount

            if lineas1>0:
                for row_number,lineaquery in enumerate(datos):
                    for row,data in enumerate(lineaquery):
                         self.tableMovs.setItem( row_number,row,QtWidgets.QTableWidgetItem(str(data)))

                self.rellenaVisual()
                cursor.close
                return lineas1

            else:
                return 0

    
    def onClickTodo(self):
        self.select_Todo()

    def onClickFlechaAd(self):
        self.campos+=1
        if self.campos>=self.lineas2:
            self.campos=0   

        self.rellenaVisual()

        

    def onClickFlechaAt(self):
        
        if self.campos<1:
            self.campos=self.lineas2
        
        self.campos-=1
        self.rellenaVisual()
        
                    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movimientos compra/venta"))
        self.label.setText(_translate("MainWindow", "Id:"))
        self.label_2.setText(_translate("MainWindow", "Factura:"))
        self.label_3.setText(_translate("MainWindow", "Precio:"))
        self.label_4.setText(_translate("MainWindow", "Cliente:"))
        self.label_5.setText(_translate("MainWindow", "Producto:"))
        self.label_6.setText(_translate("MainWindow", "Cantidad:"))
        self.label_7.setText(_translate("MainWindow", "Proveedor:"))
        self.label_8.setText(_translate("MainWindow", "Observaciones:"))
        self.label_9.setText(_translate("MainWindow", " Buscar por:"))

        
       
        
       
      

       
      

        self.cbbBuscarpor.setItemText(0, _translate("MainWindow", "Id"))
        self.cbbBuscarpor.setItemText(1, _translate("MainWindow", "Factura"))
        self.cbbBuscarpor.setItemText(2, _translate("MainWindow", "Producto"))
        self.cbbBuscarpor.setItemText(3, _translate("MainWindow", "Cantidad"))
        self.cbbBuscarpor.setItemText(4, _translate("MainWindow", "Precio"))
        self.cbbBuscarpor.setItemText(5, _translate("MainWindow", "Cliente"))
        self.cbbBuscarpor.setItemText(6, _translate("MainWindow", "Proveedor"))


        

import iconos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())