import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from NovelConverter_layout import *

exception = ['【','［','「','『','〈','〝']
restoreEpn = ['　']
isModeFormat = True

class NCWindow(QDialog, Ui_NovelConverter):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowSystemMenuHint)
        self.show()

        self.textEdit.textChanged.connect(self.convertOriginalTextToUploadFormat)
        self.pushButton.clicked.connect(self.modeChanger)
    
    def convertOriginalTextToUploadFormat(self):
        oldText = self.textEdit.toPlainText().splitlines()
        length = len(oldText)
        new = ''
        lineChange = '\n\n'

        for i, line in enumerate(oldText):
            if i == length - 1:
                lineChange = ''
            
            if line:
                if line[0] in exception:
                    new += line + lineChange
                else:
                    new += '　' + line + lineChange
            else:
                new += lineChange
        
        self.textBrowser.clear()
        self.textBrowser.append(new)

    def convertUploadFormatToOriginalText(self):
        oldText = self.textEdit.toPlainText().splitlines()
        length = len(oldText)
        new = ''
        lineChange = '\n'
        cnt = 0

        for i, line in enumerate(oldText):
            if i == length - 1:
                lineChange = ''
            
            if line:
                cnt = 0
                if line[0] in restoreEpn:
                    new += line[1:] + lineChange
                else:
                    new += line + lineChange
            else:
                cnt += 1
                if cnt > 1:
                    new += lineChange
                    cnt = 0
        
        self.textBrowser.clear()
        self.textBrowser.append(new)
    
    def modeChanger(self):
        global isModeFormat
        _translate = QtCore.QCoreApplication.translate
        if isModeFormat:
            self.textEdit.textChanged.connect(self.convertUploadFormatToOriginalText)
            self.pushButton.setText(_translate("NovelConverter", "Go to format mode"))
            isModeFormat = False
            self.textBrowser.clear()
        else:
            self.textEdit.textChanged.connect(self.convertOriginalTextToUploadFormat)
            self.pushButton.setText(_translate("NovelConverter", "Go to restore mode"))
            isModeFormat = True
            self.textBrowser.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = NCWindow()
    mywindow.show()
    app.exec_()