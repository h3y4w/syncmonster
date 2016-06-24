import pymainwindow
import pylogin
import pyfiledrop

class MAINWINDOW(object):

    def show(self):
        self.MainWindow.show()
        sys.exit(self.appMainWindow.exec_())
    def hide (self):
        self.MainWindow.hide()
    def quit (self):
        self.Main.Window.quit()
    
    def upload_button_clicked(self):
        pyfiledrop.window.show()
#class FileDrop(object)


if __name__ == "__main__":
    import sys
    MW = MAINWINDOW()   
    MW.appMainWindow = pymainwindow.QtGui.QApplication(sys.argv)
    MW.MainWindow = pymainwindow.QtGui.QMainWindow()
    uiMainWindow = pymainwindow.Ui_MainWindow()
    uiMainWindow.setupUi(MW.MainWindow)
    MW.show()
    pymainwindow.QtCore.QObject.connect(self.upload_button(), QtCore.SIGNAL(_fromUtf8("clicked()")), self.upload_button_clicked)
