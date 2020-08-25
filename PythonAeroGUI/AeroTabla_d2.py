# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AeroTabla_d2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(843, 503)
        self.bel_duracion = QtWidgets.QLabel(Form)
        self.bel_duracion.setGeometry(QtCore.QRect(630, 50, 181, 16))
        self.bel_duracion.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_duracion.setText("")
        self.bel_duracion.setObjectName("bel_duracion")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(100, 10, 431, 51))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 41))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bel_nameRoute = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bel_nameRoute.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bel_nameRoute.setStyleSheet("font: 15pt \"Ubuntu\";")
        self.bel_nameRoute.setText("")
        self.bel_nameRoute.setTextFormat(QtCore.Qt.AutoText)
        self.bel_nameRoute.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.bel_nameRoute.setObjectName("bel_nameRoute")
        self.horizontalLayout.addWidget(self.bel_nameRoute)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tablaDatos = QtWidgets.QTableWidget(Form)
        self.tablaDatos.setGeometry(QtCore.QRect(40, 100, 781, 291))
        self.tablaDatos.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.tablaDatos.setObjectName("tablaDatos")
        self.tablaDatos.setColumnCount(0)
        self.tablaDatos.setRowCount(0)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(40, 20, 71, 20))
        self.label_20.setStyleSheet("font: 15pt \"Ubuntu\";")
        self.label_20.setObjectName("label_20")
        self.bel_nameFile = QtWidgets.QLabel(Form)
        self.bel_nameFile.setGeometry(QtCore.QRect(100, 70, 431, 21))
        self.bel_nameFile.setStyleSheet("font: 15pt \"Ubuntu\";")
        self.bel_nameFile.setObjectName("bel_nameFile")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(550, 10, 81, 17))
        self.label_8.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_8.setObjectName("label_8")
        self.btn_abrirTabla = QtWidgets.QPushButton(Form)
        self.btn_abrirTabla.setGeometry(QtCore.QRect(540, 430, 131, 61))
        self.btn_abrirTabla.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_abrirTabla.setObjectName("btn_abrirTabla")
        self.bel_dateStart = QtWidgets.QLabel(Form)
        self.bel_dateStart.setGeometry(QtCore.QRect(630, 10, 181, 17))
        self.bel_dateStart.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_dateStart.setText("")
        self.bel_dateStart.setObjectName("bel_dateStart")
        self.btn_borrarNew = QtWidgets.QPushButton(Form)
        self.btn_borrarNew.setGeometry(QtCore.QRect(690, 430, 131, 61))
        self.btn_borrarNew.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_borrarNew.setObjectName("btn_borrarNew")
        self.bel_dateEnd = QtWidgets.QLabel(Form)
        self.bel_dateEnd.setGeometry(QtCore.QRect(630, 30, 181, 17))
        self.bel_dateEnd.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_dateEnd.setText("")
        self.bel_dateEnd.setObjectName("bel_dateEnd")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(550, 50, 81, 20))
        self.label_11.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(550, 30, 81, 17))
        self.label_10.setStyleSheet("font: 12pt \"Ubuntu\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(40, 70, 61, 20))
        self.label_23.setStyleSheet("font: 15pt \"Ubuntu\";")
        self.label_23.setObjectName("label_23")
        self.bel_pantalla1_6 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_6.setGeometry(QtCore.QRect(60, 400, 71, 31))
        self.bel_pantalla1_6.setStyleSheet("font: 20pt \"Ubuntu\";")
        self.bel_pantalla1_6.setObjectName("bel_pantalla1_6")
        self.bel_pantalla1_7 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_7.setGeometry(QtCore.QRect(230, 460, 41, 41))
        self.bel_pantalla1_7.setStyleSheet("font: 20pt \"Ubuntu\";")
        self.bel_pantalla1_7.setObjectName("bel_pantalla1_7")
        self.bel_CDA = QtWidgets.QLabel(Form)
        self.bel_CDA.setGeometry(QtCore.QRect(50, 430, 171, 71))
        self.bel_CDA.setStyleSheet("background-color:  rgb(114, 159, 207);\n"
"font: 50pt \"Ubuntu\";\n"
"border-radius: 10px;\n"
"padding: 4px;")
        self.bel_CDA.setText("")
        self.bel_CDA.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_CDA.setObjectName("bel_CDA")
        self.bel_pantalla1_8 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_8.setGeometry(QtCore.QRect(460, 460, 41, 41))
        self.bel_pantalla1_8.setStyleSheet("font: 20pt \"Ubuntu\";")
        self.bel_pantalla1_8.setObjectName("bel_pantalla1_8")
        self.bel_payLoad = QtWidgets.QLabel(Form)
        self.bel_payLoad.setGeometry(QtCore.QRect(280, 430, 171, 71))
        self.bel_payLoad.setStyleSheet("background-color:  rgb(114, 159, 207);\n"
"font: 50pt \"Ubuntu\";\n"
"border-radius: 10px;\n"
"padding: 4px;")
        self.bel_payLoad.setText("")
        self.bel_payLoad.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_payLoad.setObjectName("bel_payLoad")
        self.bel_pantalla1_9 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_9.setGeometry(QtCore.QRect(290, 390, 111, 41))
        self.bel_pantalla1_9.setStyleSheet("font: 20pt \"Ubuntu\";")
        self.bel_pantalla1_9.setObjectName("bel_pantalla1_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_20.setText(_translate("Form", "Route:"))
        self.bel_nameFile.setText(_translate("Form", "Roni"))
        self.label_8.setText(_translate("Form", "Date start:"))
        self.btn_abrirTabla.setText(_translate("Form", "Open Data"))
        self.btn_borrarNew.setText(_translate("Form", "Clean Data"))
        self.label_11.setText(_translate("Form", "No. Dates:"))
        self.label_10.setText(_translate("Form", "Date end:"))
        self.label_23.setText(_translate("Form", "Name:"))
        self.bel_pantalla1_6.setText(_translate("Form", "CDA "))
        self.bel_pantalla1_7.setText(_translate("Form", "[ft]"))
        self.bel_pantalla1_8.setText(_translate("Form", "[ft]"))
        self.bel_pantalla1_9.setText(_translate("Form", "Payload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

