import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton
from PyQt5.QtCore import QPoint, QSize


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.pushMeButton = QPushButton("Push Me !", self)
        self.pushMeButton.resize(QSize(200, 20))
        self.pushMeButton.move(QPoint(150, 240))

        self.connect_signals()

    def connect_signals(self):
        self.pushMeButton.clicked.connect(self.eh_pushMeButton)

    def eh_pushMeButton(self):
        self.msgPushed = QMessageBox()
        self.msgPushed.setWindowTitle("Hey !")
        self.msgPushed.setDetailedText("If you click Ok, the push button is going to be disabled.")
        self.msgPushed.setText("You pushed the button !")
        self.msgPushed.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgPushed.buttonClicked.connect(self.eh_msgPushed)
        self.msgPushed.setIcon(QMessageBox.Question)

        ''' show() doesnt block the main thread '''
        self.msgPushed.show()

        '''
        exec() [or exec_()] blocks the main thread until
        the QMessageBox returns and we can use the return value to
        get which button was pushed
        '''

        # button_pushed = self.msgPushed.exec()
        #
        # if button_pushed == QMessageBox.Ok:
        #     self.pushMeButton.setDisabled(True)

    def eh_msgPushed(self, button):
        '''
        I couldn't find a better way to get which button was pushed
        when trying to use non-blocking solution
        '''
        if button.text() == '&OK':
            self.pushMeButton.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    dialog.show()

    sys.exit(app.exec())
