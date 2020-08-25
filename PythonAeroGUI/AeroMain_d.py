# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AeroMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1010, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1010, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/Icono4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("padding:0px;\n"
"")
        MainWindow.setIconSize(QtCore.QSize(12, 12))
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Datos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Datos.setGeometry(QtCore.QRect(10, 130, 89, 81))
        self.btn_Datos.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
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
        self.btn_Datos.setObjectName("btn_Datos")
        self.btn_RecorderData = QtWidgets.QPushButton(self.centralwidget)
        self.btn_RecorderData.setGeometry(QtCore.QRect(10, 230, 89, 81))
        self.btn_RecorderData.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
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
        self.btn_RecorderData.setObjectName("btn_RecorderData")
        self.listaPantallas = QtWidgets.QStackedWidget(self.centralwidget)
        self.listaPantallas.setGeometry(QtCore.QRect(130, 0, 861, 501))
        self.listaPantallas.setToolTipDuration(0)
        self.listaPantallas.setStyleSheet("padding:0px;\n"
"\n"
"\n"
"")
        self.listaPantallas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listaPantallas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listaPantallas.setObjectName("listaPantallas")
        self.btn_Arduino = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Arduino.setGeometry(QtCore.QRect(10, 440, 71, 61))
        self.btn_Arduino.setStyleSheet("\n"
"QPushButton {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-image: url(:/AeroImagenes/ImagesAero/AeroHome.png);\n"
"border-style: outset;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/AeroCasa1.png);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 1px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-image: url(:/AeroImagenes/ImagesAero/AeroHome.png);\n"
"padding: 5px;\n"
"}\n"
"")
        self.btn_Arduino.setText("")
        self.btn_Arduino.setObjectName("btn_Arduino")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listaPantallas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UNAM Aero Design 2020"))
        self.btn_Datos.setText(_translate("MainWindow", "Data"))
        self.btn_RecorderData.setText(_translate("MainWindow", "Recorder\n"
"Data"))

import imagenes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

