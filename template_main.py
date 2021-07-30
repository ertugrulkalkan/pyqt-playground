import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QDialog


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
