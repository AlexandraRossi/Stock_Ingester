import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "HelloWorld"
        self.width = 640
        self.height = 480
        self.initUI()

    def build_menu(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu("file")
        menu_bar.addMenu("edit")
        menu_bar.addMenu("help")

        exit_button = QAction(QIcon('exit24.png'), 'Quit', self)
        exit_button.setShortcut("Ctrl-Q")
        exit_button.setStatusTip("exit application")
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0,0, self.width, self.height)
        status_bar = self.statusBar()
        status_bar.showMessage("Just a quiick hello", 2000)
        self.build_menu()

        self.show()




if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
