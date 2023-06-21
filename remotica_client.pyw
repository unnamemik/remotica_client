# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remotica_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        Form.setMinimumSize(QtCore.QSize(600, 300))
        Form.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../remotica/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 70, 381, 138))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton_OK = QtWidgets.QPushButton(Form)
        self.pushButton_OK.setGeometry(QtCore.QRect(100, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(200, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 171, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_about = QtWidgets.QPushButton(Form)
        self.pushButton_about.setGeometry(QtCore.QRect(490, 20, 101, 31))
        self.pushButton_about.setObjectName("pushButton_about")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(340, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("background-color: rgb(255, 117, 112);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(300, 260, 291, 31))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Remotica"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Settings</p></body></html>"))
        self.label_2.setText(_translate("Form", "Host IP:"))
        self.label_3.setText(_translate("Form", "Host port:"))
        self.lineEdit_2.setText(_translate("Form", "33444"))
        self.label_4.setText(_translate("Form", "Device IP:"))
        self.lineEdit_3.setText(_translate("Form", "192.168.0.112"))
        self.label_5.setText(_translate("Form", "Device port:"))
        self.lineEdit_4.setText(_translate("Form", "8266"))
        self.lineEdit.setText(_translate("Form", "31.31.196.204"))
        self.pushButton_OK.setText(_translate("Form", "OK"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.pushButton_about.setText(_translate("Form", "About"))
        self.pushButton_close.setText(_translate("Form", "Disconnect"))
        self.label_7.setText(_translate("Form", "Press to disconnect and close reliably"))