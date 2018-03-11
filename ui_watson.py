# This is an example case

import sys, json
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username = 'cc6f56ad-4c66-4478-a59f-6fa3f3be4fa0',
    password = 'B1o1dKCeWkG3',
    version = '2018-02-16'
)

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
    response = conversation.list_workspaces()
    print(json.dumps(response, indent=2))
    # check the output from your terminal. remember the workspace_id of your testing workspace!
    # in my case, it is 6889f7cc-48a7-49f4-b16c-9b7cb410b564

    response = conversation.message(
        workspace_id='6889f7cc-48a7-49f4-b16c-9b7cb410b564',
        input={
            'text': 'I want yellow'
        }
    )
    print ('I think you want color: ',response['entities'][0]['value'])

    print(json.dumps(response, indent=2))


    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())