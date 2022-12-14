# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication

class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 436)
        MainWindow.setMinimumSize(QtCore.QSize(445, 436))
        MainWindow.setMaximumSize(QtCore.QSize(445, 436))
        MainWindow.setStyleSheet("background-color: rgb(255, 221, 119);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.P2_label_10 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_10.setGeometry(QtCore.QRect(260, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_10.setFont(font)
        self.P2_label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_10.setStyleSheet("color: rgb(255, 255, 0);")
        self.P2_label_10.setScaledContents(False)
        self.P2_label_10.setObjectName("P2_label_10")
        self.P2_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_7.setGeometry(QtCore.QRect(170, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_7.setFont(font)
        self.P2_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_7.setStyleSheet("color: rgb(255, 255, 0);")
        self.P2_label_7.setScaledContents(False)
        self.P2_label_7.setObjectName("P2_label_7")
        self.P2_label_11 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_11.setGeometry(QtCore.QRect(290, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_11.setFont(font)
        self.P2_label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_11.setStyleSheet("color: rgb(255, 0, 0);")
        self.P2_label_11.setScaledContents(False)
        self.P2_label_11.setObjectName("P2_label_11")
        self.P2_label_9 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_9.setGeometry(QtCore.QRect(230, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_9.setFont(font)
        self.P2_label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_9.setStyleSheet("color: rgb(255, 152, 34);")
        self.P2_label_9.setScaledContents(False)
        self.P2_label_9.setObjectName("P2_label_9")
        self.P2_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_6.setGeometry(QtCore.QRect(140, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_6.setFont(font)
        self.P2_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_6.setStyleSheet("color: rgb(255, 152, 34);")
        self.P2_label_6.setScaledContents(False)
        self.P2_label_6.setObjectName("P2_label_6")
        self.P2_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.P2_label_8.setGeometry(QtCore.QRect(200, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.P2_label_8.setFont(font)
        self.P2_label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.P2_label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.P2_label_8.setScaledContents(False)
        self.P2_label_8.setObjectName("P2_label_8")
        self.player_label = QtWidgets.QLabel(self.centralwidget)
        self.player_label.setGeometry(QtCore.QRect(80, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.player_label.setFont(font)
        self.player_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.player_label.setStyleSheet("")
        self.player_label.setScaledContents(False)
        self.player_label.setObjectName("player_label")
        self.player_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.player_label_2.setGeometry(QtCore.QRect(80, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.player_label_2.setFont(font)
        self.player_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.player_label_2.setStyleSheet("")
        self.player_label_2.setScaledContents(False)
        self.player_label_2.setObjectName("player_label_2")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(220, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.user_name.setObjectName("user_name")
        self.user_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.user_pass.setGeometry(QtCore.QRect(220, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_pass.setFont(font)
        self.user_pass.setObjectName("user_pass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(200, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("background-color: rgb(255, 147, 23);")
        self.btn_login.setObjectName("btn_login")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(270, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("background-color: rgb(255, 147, 23);")
        self.btn_signup.setObjectName("btn_signup")
        self.player_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.player_label_3.setGeometry(QtCore.QRect(100, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player_label_3.setFont(font)
        self.player_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.player_label_3.setStyleSheet("")
        self.player_label_3.setScaledContents(False)
        self.player_label_3.setObjectName("player_label_3")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(170, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_error.setFont(font)
        self.lbl_error.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_error.setStyleSheet("")
        self.lbl_error.setText("")
        self.lbl_error.setScaledContents(False)
        self.lbl_error.setObjectName("lbl_error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.P2_label_10.setText(_translate("MainWindow", "K"))
        self.P2_label_7.setText(_translate("MainWindow", "E"))
        self.P2_label_11.setText(_translate("MainWindow", "E"))
        self.P2_label_9.setText(_translate("MainWindow", "U"))
        self.P2_label_6.setText(_translate("MainWindow", "P"))
        self.P2_label_8.setText(_translate("MainWindow", "R"))
        self.player_label.setText(_translate("MainWindow", "User name"))
        self.player_label_2.setText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_signup.setText(_translate("MainWindow", "SignUp"))
        self.player_label_3.setText(_translate("MainWindow", "Don\'t have account?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
