# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/factura.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(220, 20, 121, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 20))
        self.label_2.setObjectName("label_2")
        self.recibe_nombre_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_cliente.setGeometry(QtCore.QRect(150, 80, 311, 21))
        self.recibe_nombre_cliente.setObjectName("recibe_nombre_cliente")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(530, 40, 121, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.btn_crear_factura = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crear_factura.setGeometry(QtCore.QRect(240, 110, 91, 31))
        self.btn_crear_factura.setObjectName("btn_crear_factura")
        self.btn_buscar_factura = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar_factura.setGeometry(QtCore.QRect(200, 240, 101, 31))
        self.btn_buscar_factura.setObjectName("btn_buscar_factura")
        self.nombre_cliente = QtWidgets.QLabel(self.centralwidget)
        self.nombre_cliente.setGeometry(QtCore.QRect(570, 80, 47, 13))
        self.nombre_cliente.setObjectName("nombre_cliente")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(150, 160, 121, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.mostrar_cliente_factura = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_cliente_factura.setGeometry(QtCore.QRect(590, 170, 151, 16))
        self.mostrar_cliente_factura.setObjectName("mostrar_cliente_factura")
        self.mostrar_total_factura = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_total_factura.setGeometry(QtCore.QRect(590, 210, 131, 16))
        self.mostrar_total_factura.setObjectName("mostrar_total_factura")
        self.mostrar_productos_factura = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_productos_factura.setGeometry(QtCore.QRect(120, 290, 951, 21))
        self.mostrar_productos_factura.setObjectName("mostrar_productos_factura")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(260, 340, 121, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(280, 450, 121, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 410, 61, 16))
        self.label_11.setObjectName("label_11")
        self.recibe_cedula_buscar_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_cedula_buscar_3.setGeometry(QtCore.QRect(270, 410, 311, 21))
        self.recibe_cedula_buscar_3.setObjectName("recibe_cedula_buscar_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(190, 520, 47, 13))
        self.label_12.setObjectName("label_12")
        self.recibe_cedula_buscar_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_cedula_buscar_4.setGeometry(QtCore.QRect(280, 520, 311, 21))
        self.recibe_cedula_buscar_4.setObjectName("recibe_cedula_buscar_4")
        self.btn_eliminar_factura = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eliminar_factura.setGeometry(QtCore.QRect(640, 410, 75, 23))
        self.btn_eliminar_factura.setObjectName("btn_eliminar_factura")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 520, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.recibe_id_factura = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_id_factura.setGeometry(QtCore.QRect(80, 200, 311, 21))
        self.recibe_id_factura.setObjectName("recibe_id_factura")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 51, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(450, 160, 121, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(450, 200, 121, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(390, 250, 121, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.mostrar_total_factura_2 = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_total_factura_2.setGeometry(QtCore.QRect(540, 450, 131, 16))
        self.mostrar_total_factura_2.setObjectName("mostrar_total_factura_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">crear factura</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "cliente_id"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">codigo factura</span></p></body></html>"))
        self.btn_crear_factura.setText(_translate("MainWindow", "crear"))
        self.btn_buscar_factura.setText(_translate("MainWindow", "buscar"))
        self.nombre_cliente.setText(_translate("MainWindow", "TextLabel"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">buscar factura</span></p></body></html>"))
        self.mostrar_cliente_factura.setText(_translate("MainWindow", "TextLabel"))
        self.mostrar_total_factura.setText(_translate("MainWindow", "TextLabel"))
        self.mostrar_productos_factura.setText(_translate("MainWindow", "TextLabel"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Eliminar factura</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Eliminar facturas cliente</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "factura_id"))
        self.label_12.setText(_translate("MainWindow", "cliente_id"))
        self.btn_eliminar_factura.setText(_translate("MainWindow", "eliminar"))
        self.pushButton_4.setText(_translate("MainWindow", "eliminar"))
        self.label_3.setText(_translate("MainWindow", "factura_id"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">cliente:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">total:</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">productos:</span></p></body></html>"))
        self.mostrar_total_factura_2.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
