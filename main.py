from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import os

includePath = os.path.abspath(os.getcwd() + '\\Include')
sys.path.append(includePath)

from PTP import PDFToPicture

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFToPicture()
    window.show()
    app.exec_()
