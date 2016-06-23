from PyQt5 import uic, QtWidgets
import sys

class Ui(QtWidgets.QDialog):
    def __init__ (self):
        super(Ui, self).__init__()
        uic.loadUi('login.ui', self)
        self.show()
        self.Connect(SIGNAL("clicked()"), self.login_click)
    def login_click(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
