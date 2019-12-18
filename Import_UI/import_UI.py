import sys
from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import *
qtCreatorFile = "import_UI.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    try:
        main()
    except Exception as e:
        print(e)
