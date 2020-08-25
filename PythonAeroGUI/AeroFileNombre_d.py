# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AeroFileNombre_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 227)
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label_23.setObjectName("label_23")
        self.lineEdit_nombre = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(110, 40, 241, 25))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.bel_estadoNombre = QtWidgets.QLabel(Dialog)
        self.bel_estadoNombre.setGeometry(QtCore.QRect(20, 80, 321, 91))
        self.bel_estadoNombre.setText("")
        self.bel_estadoNombre.setObjectName("bel_estadoNombre")
        self.btn_endSetName = QtWidgets.QPushButton(Dialog)
        self.btn_endSetName.setGeometry(QtCore.QRect(170, 180, 89, 25))
        self.btn_endSetName.setObjectName("btn_endSetName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EditName"))
        self.label_23.setText(_translate("Dialog", "New name:"))
        self.btn_endSetName.setText(_translate("Dialog", "Finalize"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

