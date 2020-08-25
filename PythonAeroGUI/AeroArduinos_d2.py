# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AeroArduinos_d2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 504)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, -30, 621, 451))
        self.label.setStyleSheet("border-image: url(:/AeroImagenes/ImagesAero/Aero_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 310, 621, 191))
        self.groupBox_2.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_20.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_20.setObjectName("label_20")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(10, 90, 51, 20))
        self.label_23.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_23.setObjectName("label_23")
        self.btn_Conectar = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_Conectar.setGeometry(QtCore.QRect(320, 150, 31, 31))
        self.btn_Conectar.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"/*color: #333;*/\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_clicNegro.png);\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_clicRosa.png);\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_clicNegro.png);\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_Conectar.setText("")
        self.btn_Conectar.setObjectName("btn_Conectar")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(280, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.cmbBox_velocidad = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbBox_velocidad.setGeometry(QtCore.QRect(90, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cmbBox_velocidad.setFont(font)
        self.cmbBox_velocidad.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.cmbBox_velocidad.setObjectName("cmbBox_velocidad")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.cmbBox_velocidad.addItem("")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(10, 150, 81, 31))
        self.label_25.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_25.setObjectName("label_25")
        self.btn_routeFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_routeFile.setGeometry(QtCore.QRect(390, 80, 41, 51))
        self.btn_routeFile.setStyleSheet("QPushButton {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_logo5.png);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_logo4.png);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/Aero_logo5.png);\n"
"padding: 5px;\n"
"}\n"
"")
        self.btn_routeFile.setText("")
        self.btn_routeFile.setObjectName("btn_routeFile")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(440, 70, 171, 111))
        self.groupBox_5.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.groupBox_5.setObjectName("groupBox_5")
        self.bel_Arduino = QtWidgets.QLabel(self.groupBox_5)
        self.bel_Arduino.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.bel_Arduino.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_Arduino.setText("")
        self.bel_Arduino.setObjectName("bel_Arduino")
        self.bel_pantalla1 = QtWidgets.QLabel(self.groupBox_5)
        self.bel_pantalla1.setGeometry(QtCore.QRect(10, 60, 121, 17))
        self.bel_pantalla1.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_pantalla1.setText("")
        self.bel_pantalla1.setObjectName("bel_pantalla1")
        self.bel_pantalla2 = QtWidgets.QLabel(self.groupBox_5)
        self.bel_pantalla2.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.bel_pantalla2.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_pantalla2.setText("")
        self.bel_pantalla2.setObjectName("bel_pantalla2")
        self.proBar_carga = QtWidgets.QProgressBar(self.groupBox_5)
        self.proBar_carga.setGeometry(QtCore.QRect(140, 20, 31, 91))
        self.proBar_carga.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.proBar_carga.setProperty("value", 0)
        self.proBar_carga.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.proBar_carga.setOrientation(QtCore.Qt.Vertical)
        self.proBar_carga.setInvertedAppearance(True)
        self.proBar_carga.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.proBar_carga.setObjectName("proBar_carga")
        self.btn_nameFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_nameFile.setGeometry(QtCore.QRect(310, 80, 41, 41))
        self.btn_nameFile.setStyleSheet("/*\n"
"\n"
"background-image: url(:/AeroImagenes/ImagesAero/aeroPencilBLue1.png);\n"
"*/\n"
"QPushButton {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/pencilBlue.png);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"    border-image: url(:/AeroImagenes/ImagesAero/aeroPencilBLue1.png);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/pencilBlue.png);\n"
"padding: 5px;\n"
"}\n"
"")
        self.btn_nameFile.setText("")
        self.btn_nameFile.setObjectName("btn_nameFile")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(70, 30, 521, 41))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 36))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_route = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.name_route.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.name_route.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.name_route.setText("")
        self.name_route.setTextFormat(QtCore.Qt.AutoText)
        self.name_route.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.name_route.setObjectName("name_route")
        self.horizontalLayout.addWidget(self.name_route)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bel_nameFile = QtWidgets.QLabel(self.groupBox_2)
        self.bel_nameFile.setGeometry(QtCore.QRect(70, 90, 221, 21))
        self.bel_nameFile.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_nameFile.setObjectName("bel_nameFile")

        self.retranslateUi(Form)
        self.cmbBox_velocidad.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Dates Fight:"))
        self.label_20.setText(_translate("Form", "Route:"))
        self.label_23.setText(_translate("Form", "Name:"))
        self.label_24.setText(_translate("Form", "[Bd]"))
        self.cmbBox_velocidad.setItemText(0, _translate("Form", "300"))
        self.cmbBox_velocidad.setItemText(1, _translate("Form", "1,200"))
        self.cmbBox_velocidad.setItemText(2, _translate("Form", "2,400"))
        self.cmbBox_velocidad.setItemText(3, _translate("Form", "4,800"))
        self.cmbBox_velocidad.setItemText(4, _translate("Form", "9,600"))
        self.cmbBox_velocidad.setItemText(5, _translate("Form", "19,200"))
        self.cmbBox_velocidad.setItemText(6, _translate("Form", "38,400"))
        self.cmbBox_velocidad.setItemText(7, _translate("Form", "57,600"))
        self.cmbBox_velocidad.setItemText(8, _translate("Form", "74,880"))
        self.cmbBox_velocidad.setItemText(9, _translate("Form", "115,200"))
        self.label_25.setText(_translate("Form", "Baud Rate:"))
        self.groupBox_5.setTitle(_translate("Form", "Charged devices"))
        self.proBar_carga.setFormat(_translate("Form", "%p%"))
        self.bel_nameFile.setText(_translate("Form", "Nombre.aeron"))

import imagenes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

