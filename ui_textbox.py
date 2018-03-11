import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()

        if self.aggresive_polite(textboxValue) == -1:
            QMessageBox.question(self, 'Message - pythonspot.com', "Your message is aggresive" , QMessageBox.Ok,
                                 QMessageBox.Ok)
        elif self.aggresive_polite(textboxValue) == 1:
            QMessageBox.question(self, 'Message - pythonspot.com', "Your message is polite", QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'Message - pythonspot.com', "Your message is neutral", QMessageBox.Ok,
                                 QMessageBox.Ok)

        self.textbox.setText("")

    def aggresive_polite(self, message):
        # your method from the interactive agent example.
        return -1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())