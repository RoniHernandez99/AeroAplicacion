# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AeroAccion_d2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(859, 507)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(380, 10, 441, 221))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_5.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 17))
        self.label_4.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 17))
        self.label_3.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.belData1_long = QtWidgets.QLabel(self.groupBox)
        self.belData1_long.setGeometry(QtCore.QRect(120, 40, 171, 17))
        self.belData1_long.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.belData1_long.setObjectName("belData1_long")
        self.belData2_lat = QtWidgets.QLabel(self.groupBox)
        self.belData2_lat.setGeometry(QtCore.QRect(120, 80, 171, 17))
        self.belData2_lat.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.belData2_lat.setObjectName("belData2_lat")
        self.belData3_velo = QtWidgets.QLabel(self.groupBox)
        self.belData3_velo.setGeometry(QtCore.QRect(120, 120, 171, 17))
        self.belData3_velo.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.belData3_velo.setObjectName("belData3_velo")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 91, 51))
        self.label_6.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_6.setObjectName("label_6")
        self.belData_dist = QtWidgets.QLabel(self.groupBox)
        self.belData_dist.setGeometry(QtCore.QRect(120, 180, 191, 17))
        self.belData_dist.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.belData_dist.setObjectName("belData_dist")
        self.bel_pantalla1_4 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_4.setGeometry(QtCore.QRect(350, 340, 121, 51))
        self.bel_pantalla1_4.setStyleSheet("font: 40pt \"Ubuntu\";")
        self.bel_pantalla1_4.setObjectName("bel_pantalla1_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 341, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(50, 30, 121, 17))
        self.label_12.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.label_12.setObjectName("label_12")
        self.belTimeVuelo = QtWidgets.QLabel(self.groupBox_2)
        self.belTimeVuelo.setGeometry(QtCore.QRect(180, 30, 121, 21))
        self.belTimeVuelo.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.belTimeVuelo.setText("")
        self.belTimeVuelo.setObjectName("belTimeVuelo")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(310, 30, 21, 17))
        self.label_14.setObjectName("label_14")
        self.btn_startPause = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_startPause.setGeometry(QtCore.QRect(10, 50, 111, 51))
        self.btn_startPause.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.btn_startPause.setObjectName("btn_startPause")
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 170, 111, 51))
        self.btn_cancel.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_terminar = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_terminar.setGeometry(QtCore.QRect(10, 110, 111, 51))
        self.btn_terminar.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.btn_terminar.setObjectName("btn_terminar")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(160, 80, 171, 91))
        self.groupBox_5.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.groupBox_5.setObjectName("groupBox_5")
        self.bel_Arduino = QtWidgets.QLabel(self.groupBox_5)
        self.bel_Arduino.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.bel_Arduino.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_Arduino.setText("")
        self.bel_Arduino.setObjectName("bel_Arduino")
        self.bel_pantalla1 = QtWidgets.QLabel(self.groupBox_5)
        self.bel_pantalla1.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.bel_pantalla1.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.bel_pantalla1.setText("")
        self.bel_pantalla1.setObjectName("bel_pantalla1")
        self.bel_pantalla2 = QtWidgets.QLabel(self.groupBox_5)
        self.bel_pantalla2.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.bel_pantalla2.setStyleSheet("font: 12pt \"Ubuntu\";\n"
"")
        self.bel_pantalla2.setText("")
        self.bel_pantalla2.setObjectName("bel_pantalla2")
        self.proBar_carga = QtWidgets.QProgressBar(self.groupBox_5)
        self.proBar_carga.setGeometry(QtCore.QRect(140, 20, 31, 71))
        self.proBar_carga.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.proBar_carga.setProperty("value", 0)
        self.proBar_carga.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.proBar_carga.setOrientation(QtCore.Qt.Vertical)
        self.proBar_carga.setInvertedAppearance(True)
        self.proBar_carga.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.proBar_carga.setObjectName("proBar_carga")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 20, 341, 51))
        self.scrollArea_2.setStyleSheet("padding-top: 0px;\n"
"padding-right: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 0px;\n"
" ")
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 41))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bel_nameFile = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.bel_nameFile.setStyleSheet("font: 15pt \"Ubuntu\";\n"
"padding-top: 0px;\n"
"padding-right: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 0px;\n"
"\n"
"margin-top: 0px;\n"
"margin-right: 0px;\n"
"margin-bottom: 0px;\n"
"margin-left: 0px;\n"
"\n"
" ")
        self.bel_nameFile.setText("")
        self.bel_nameFile.setObjectName("bel_nameFile")
        self.horizontalLayout_2.addWidget(self.bel_nameFile)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.bel_pantalla1_5 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_5.setGeometry(QtCore.QRect(220, 440, 81, 61))
        self.bel_pantalla1_5.setStyleSheet("font: 30pt \"Ubuntu\";")
        self.bel_pantalla1_5.setObjectName("bel_pantalla1_5")
        self.bel_payLoad = QtWidgets.QLabel(Form)
        self.bel_payLoad.setGeometry(QtCore.QRect(570, 400, 201, 91))
        self.bel_payLoad.setStyleSheet("background-color:  rgb(114, 159, 207);\n"
"font: 60pt \"Ubuntu\";\n"
"border-radius: 10px;\n"
"padding: 4px;")
        self.bel_payLoad.setText("")
        self.bel_payLoad.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_payLoad.setObjectName("bel_payLoad")
        self.bel_altitude = QtWidgets.QLabel(Form)
        self.bel_altitude.setGeometry(QtCore.QRect(20, 400, 201, 91))
        self.bel_altitude.setStyleSheet("background-color:  rgb(114, 159, 207);\n"
"font: 60pt \"Ubuntu\";\n"
"border-radius: 10px;\n"
"padding: 4px;")
        self.bel_altitude.setText("")
        self.bel_altitude.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_altitude.setObjectName("bel_altitude")
        self.bel_pantalla1_6 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_6.setGeometry(QtCore.QRect(590, 320, 211, 91))
        self.bel_pantalla1_6.setStyleSheet("font: 40pt \"Ubuntu\";")
        self.bel_pantalla1_6.setObjectName("bel_pantalla1_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 350, 211, 41))
        self.label_7.setStyleSheet("font: 40pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.bel_CDA = QtWidgets.QLabel(Form)
        self.bel_CDA.setGeometry(QtCore.QRect(310, 400, 201, 91))
        self.bel_CDA.setStyleSheet("background-color:  rgb(114, 159, 207);\n"
"font: 60pt \"Ubuntu\";\n"
"border-radius: 10px;\n"
"padding: 4px;")
        self.bel_CDA.setText("")
        self.bel_CDA.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_CDA.setObjectName("bel_CDA")
        self.bel_pantalla1_7 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_7.setGeometry(QtCore.QRect(510, 440, 81, 61))
        self.bel_pantalla1_7.setStyleSheet("font: 30pt \"Ubuntu\";")
        self.bel_pantalla1_7.setObjectName("bel_pantalla1_7")
        self.bel_pantalla1_8 = QtWidgets.QLabel(Form)
        self.bel_pantalla1_8.setGeometry(QtCore.QRect(770, 440, 81, 61))
        self.bel_pantalla1_8.setStyleSheet("font: 30pt \"Ubuntu\";")
        self.bel_pantalla1_8.setObjectName("bel_pantalla1_8")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 210, 231, 161))
        self.label.setStyleSheet("border-image: url(:/AeroImagenes/ImagesAero/Planeador-para-interfaz.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Primary Aircraft Data"))
        self.label_5.setText(_translate("Form", "Lng[Deg]:"))
        self.label_4.setText(_translate("Form", "Lat[Deg]:"))
        self.label_3.setText(_translate("Form", "Speed[ft/s]:"))
        self.belData1_long.setText(_translate("Form", "150"))
        self.belData2_lat.setText(_translate("Form", "150"))
        self.belData3_velo.setText(_translate("Form", "11550"))
        self.label_6.setText(_translate("Form", "Distance\n"
"to target: "))
        self.belData_dist.setText(_translate("Form", "1550"))
        self.bel_pantalla1_4.setText(_translate("Form", "CDA "))
        self.groupBox_2.setTitle(_translate("Form", "Record Flight Data"))
        self.label_12.setText(_translate("Form", "Recording time:"))
        self.label_14.setText(_translate("Form", "[s]"))
        self.btn_startPause.setText(_translate("Form", "Start"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
        self.btn_terminar.setText(_translate("Form", "FinishSave"))
        self.groupBox_5.setTitle(_translate("Form", "Charged devices"))
        self.proBar_carga.setFormat(_translate("Form", "%p%"))
        self.bel_pantalla1_5.setText(_translate("Form", "[ft]"))
        self.bel_pantalla1_6.setText(_translate("Form", "Payload"))
        self.label_7.setText(_translate("Form", "Altitude"))
        self.bel_pantalla1_7.setText(_translate("Form", "[ft]"))
        self.bel_pantalla1_8.setText(_translate("Form", "[ft]"))

import imagenes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

