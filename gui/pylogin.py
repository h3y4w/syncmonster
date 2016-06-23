# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymainwindow
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.email_label = QtGui.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(30, 170, 59, 16))
        self.email_label.setObjectName(_fromUtf8("email_label"))
        self.password_label = QtGui.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(30, 200, 61, 16))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.email_input = QtGui.QLineEdit(Dialog)
        self.email_input.setGeometry(QtCore.QRect(70, 170, 181, 21))
        self.email_input.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email_input.setObjectName(_fromUtf8("email_input"))
        self.password_input = QtGui.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(100, 200, 151, 21))
        self.password_input.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.password_input.setText(_fromUtf8(""))
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.login_button = QtGui.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(260, 180, 113, 32))
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.syncmonster_label = QtGui.QLabel(Dialog)
        self.syncmonster_label.setGeometry(QtCore.QRect(10, 280, 161, 16))
        self.syncmonster_label.setObjectName(_fromUtf8("syncmonster_label"))

        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.login_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login_button_click)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def login_button_click(self):

        email = self.email_input.text()
        password = self.password_input.text()
        exit(1)
        Dialog.close()
        pywindowmain.MainWindow.show()
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.email_label.setText(_translate("Dialog", "Email:", None))
        self.password_label.setText(_translate("Dialog", "Password:", None))
        self.login_button.setText(_translate("Dialog", "Login", None))
        self.syncmonster_label.setText(_translate("Dialog", "SyncMonster", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

