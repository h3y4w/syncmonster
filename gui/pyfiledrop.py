import sys
import objc
import CoreFoundation as CF
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyListWidget(QListWidget):
    def __init__(self, parent):
        super(MyListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

    def getUrlFromLocalFileID(self, localFileID):
        localFileQString = QString(localFileID.toLocalFile())
        relCFStringRef = CF.CFStringCreateWithCString(
            CF.kCFAllocatorDefault,
            localFileQString.toUtf8(),
            CF.kCFStringEncodingUTF8
            )
        relCFURL = CF.CFURLCreateWithFileSystemPath(
            CF.kCFAllocatorDefault,
            relCFStringRef,
            CF.kCFURLPOSIXPathStyle,
            False   # is directory
            )
        absCFURL = CF.CFURLCreateFilePathURL(
            CF.kCFAllocatorDefault,
            relCFURL,
            objc.NULL
            )
        return QUrl(str(absCFURL[0])).toLocalFile()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(MyListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(MyListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                if QString(url.toLocalFile()).startsWith('/.file/id='):
                    url = self.getUrlFromLocalFileID(url)
                    links.append(url)
                else:
                    links.append(str(url.toLocalFile()))
            for link in links:
                self.addItem(link)
        else:
            super(MyListWidget,self).dropEvent(event)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(100,100,300,400)
        self.setWindowTitle("Filenames")

        self.list = MyListWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.list)

        self.setLayout(layout)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
