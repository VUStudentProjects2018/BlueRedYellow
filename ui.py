import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com' # task 2: change the title to blue-red-yellow
        self.left = 10
        self.top = 10
        self.width = 640 # task 1: change the window size to 500 * 500
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('I am a system message!') # change the status
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
