import sys

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        # create buttons dynamically
        self.buttons = []
        for i in range(5):
            button = QPushButton(f"Button{i + 1}", self)
            button.resize(QSize(150, 50))
            button.move(QPoint(175, 25 + (100 * i)))
            self.buttons.append(button)

        self.connect_signals()
        self.show()

    def connect_signals(self):
        '''
        for button in self.buttons:                                     # wrong
            button.clicked.connect(lambda: button.setDisabled(True))    # wrong

        instead of calling button.setDisabled method
        we call the sender objects setDisabled method
        otherwise the call always sets the last button disabled.

        button variable will be always the last button on the list when the
        loop end.
        '''

        for button in self.buttons:
            button.clicked.connect(lambda: self.sender().setDisabled(True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
