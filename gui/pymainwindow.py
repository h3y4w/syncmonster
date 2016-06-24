# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.MainTabs = QtGui.QTabWidget(self.centralwidget)
        self.MainTabs.setGeometry(QtCore.QRect(30, 20, 721, 431))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.MainTabs.setFont(font)
        self.MainTabs.setObjectName(_fromUtf8("MainTabs"))
        self.home_tab = QtGui.QWidget()
        self.home_tab.setAccessibleName(_fromUtf8(""))
        self.home_tab.setAutoFillBackground(False)
        self.home_tab.setObjectName(_fromUtf8("home_tab"))
        self.MainTabs.addTab(self.home_tab, _fromUtf8(""))
        self.upload_tab = QtGui.QWidget()
        self.upload_tab.setObjectName(_fromUtf8("upload_tab"))
        self.add_file_button = QtGui.QPushButton(self.upload_tab)
        self.add_file_button.setGeometry(QtCore.QRect(20, 290, 231, 32))
        self.add_file_button.setObjectName(_fromUtf8("add_file_button"))
        self.upload_button = QtGui.QPushButton(self.upload_tab)
        self.upload_button.setGeometry(QtCore.QRect(440, 290, 251, 32))
        self.upload_button.setObjectName(_fromUtf8("upload_button"))
        self.file_list = QtGui.QListWidget(self.upload_tab)
        self.file_list.setGeometry(QtCore.QRect(20, 30, 671, 251))
        self.file_list.setObjectName(_fromUtf8("file_list"))
        self.MainTabs.addTab(self.upload_tab, _fromUtf8(""))
        self.files_tab = QtGui.QWidget()
        self.files_tab.setObjectName(_fromUtf8("files_tab"))
        self.MainTabs.addTab(self.files_tab, _fromUtf8(""))
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName(_fromUtf8("settings_tab"))
        self.password_box = QtGui.QGroupBox(self.settings_tab)
        self.password_box.setGeometry(QtCore.QRect(20, 30, 271, 331))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.password_box.setFont(font)
        self.password_box.setObjectName(_fromUtf8("password_box"))
        self.old_password_input = QtGui.QLineEdit(self.password_box)
        self.old_password_input.setGeometry(QtCore.QRect(120, 60, 113, 21))
        self.old_password_input.setObjectName(_fromUtf8("old_password_input"))
        self.new_password_input = QtGui.QLineEdit(self.password_box)
        self.new_password_input.setGeometry(QtCore.QRect(120, 100, 113, 21))
        self.new_password_input.setObjectName(_fromUtf8("new_password_input"))
        self.new_password_again_input = QtGui.QLineEdit(self.password_box)
        self.new_password_again_input.setGeometry(QtCore.QRect(120, 140, 113, 21))
        self.new_password_again_input.setObjectName(_fromUtf8("new_password_again_input"))
        self.old_password_label = QtGui.QLabel(self.password_box)
        self.old_password_label.setGeometry(QtCore.QRect(20, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.old_password_label.setFont(font)
        self.old_password_label.setObjectName(_fromUtf8("old_password_label"))
        self.new_password_label = QtGui.QLabel(self.password_box)
        self.new_password_label.setGeometry(QtCore.QRect(10, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_password_label.setFont(font)
        self.new_password_label.setObjectName(_fromUtf8("new_password_label"))
        self.new_password_again_label = QtGui.QLabel(self.password_box)
        self.new_password_again_label.setGeometry(QtCore.QRect(68, 140, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_password_again_label.setFont(font)
        self.new_password_again_label.setObjectName(_fromUtf8("new_password_again_label"))
        self.change_password_button = QtGui.QPushButton(self.password_box)
        self.change_password_button.setGeometry(QtCore.QRect(120, 170, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change_password_button.setFont(font)
        self.change_password_button.setObjectName(_fromUtf8("change_password_button"))
        self.line = QtGui.QFrame(self.settings_tab)
        self.line.setGeometry(QtCore.QRect(300, 50, 16, 311))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.MainTabs.addTab(self.settings_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.home_tab), _translate("MainWindow", "Home", None))
        self.add_file_button.setText(_translate("MainWindow", "Add File", None))
        self.upload_button.setText(_translate("MainWindow", "Upload", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.upload_tab), _translate("MainWindow", "Upload", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.files_tab), _translate("MainWindow", "Files", None))
        self.password_box.setTitle(_translate("MainWindow", "Password", None))
        self.old_password_label.setText(_translate("MainWindow", "Old Password:", None))
        self.new_password_label.setText(_translate("MainWindow", "New Password: ", None))
        self.new_password_again_label.setText(_translate("MainWindow", "Again:", None))
        self.change_password_button.setText(_translate("MainWindow", "Change", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.settings_tab), _translate("MainWindow", "Settings", None))

