from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from getpass import getuser
from PyQt5 import QtGui
from PIL import Image
from sys import argv
from os import getcwd, mkdir, listdir, path

class PDFToPicture(QMainWindow):
    def __init__(self):
        super(PDFToPicture, self).__init__()
        loadUi('UI\\Main.ui', self)

        self.setWindowIcon(QtGui.QIcon(getcwd() + '\\Img\\WHI3PER.ico'))
        self.CREATE_IN.insert('C:\\Users\\' + getuser() + '\\Desktop\\PTP\\Result.pdf')
        
        self.CONVERT.clicked.connect(self.convert)
        self.ABOUT.triggered.connect(self.aboutMe)

    # ============================================================================================== #
    
    def aboutMe(self):
        loadUi('UI\\About Me.ui', self)
        self.LOGO_LABEL.setPixmap(QPixmap(getcwd() + '\\Img\\WHI3PER.png'))
        self.EMAIL.setPixmap(QPixmap(getcwd() + '\\Img\\Gmail.png'))
        self.GITHUB.setPixmap(QPixmap(getcwd() + '\\Img\\Github.png'))
        self.LINKDIN.setPixmap(QPixmap(getcwd() + '\\Img\\Linkdin.png'))
        self.TELEGRAM.setPixmap(QPixmap(getcwd() + '\\Img\\Telegram.png'))

    # ============================================================================================== #

    def convert(self):
        try:
            picturesList = []
            picturesLocation = self.PIC_LOCATION.text()
            PDFLocation = self.CREATE_IN.text()
            
            if picturesLocation[-2:] != '\\':
                picturesLocation = picturesLocation + '\\'

            if not path.exists(PDFLocation[0:PDFLocation.rfind('\\')]):
                mkdir(PDFLocation[0:PDFLocation.rfind('\\')])
            
            for item in listdir(picturesLocation):
                picturesList.append(Image.open(picturesLocation + item).convert('RGB'))
                
            picturesList[0].save(PDFLocation, save_all = True, append_images = picturesList[1:len(picturesList)])

            message = QMessageBox()
            message.setWindowIcon(QtGui.QIcon(getcwd() + '\\Img\\WHI3PER.ico'))
            message.setWindowTitle('Result')
            message.setIcon(QMessageBox.Information)
            message.setText('Success.')
            message.exec_()
            
        except:
            message = QMessageBox()
            message.setWindowIcon(QtGui.QIcon(getcwd() + '\\Img\\WHI3PER.ico'))
            message.setWindowTitle('Result')
            message.setIcon(QMessageBox.Critical)
            message.setText('Error:\n~ Pictures not founded.\n~ Invalid path.')
            message.exec_()
            
    # ============================================================================================== #
