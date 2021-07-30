import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QSize


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

    def connect_signals(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    dialog.connect_signals()
    dialog.show()

    sys.exit(app.exec())
