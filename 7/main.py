import sys

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QCheckBox, QDialog


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.checkBox = QCheckBox("Check Box", self)
        self.checkBox.move(QPoint(100, 100))

        self.tristateCheckBox = QCheckBox("Tristate Check Box", self)
        self.tristateCheckBox.move(100, 125)
        self.tristateCheckBox.setTristate(True)
        self.tristateCheckBox.setDisabled(True)

        self.connect_signals()
        self.show()

    def connect_signals(self):
        '''
        I think its better to use toggled and stateChanged signals
        because it doesnt matter why the state changed (internal or external),
        the GUI should handle the signal. Otherwise this may be cause a bug.

        To use clicked signal, be sure what you are doing.
        '''
        # self.checkBox.clicked.connect(self.eh_checkBox_toggled)
        self.checkBox.toggled.connect(self.eh_checkBox_toggled)
        self.tristateCheckBox.stateChanged.connect(self.eh_tristateCheckBox_stateChanged)

    def eh_checkBox_toggled(self, state):
        self.tristateCheckBox.setEnabled(True) if state else self.tristateCheckBox.setDisabled(True)

    def eh_tristateCheckBox_stateChanged(self, state):
        if state == 0:
            self.checkBox.setEnabled(True)
        elif state == 1:
            self.checkBox.setEnabled(True)
        elif state == 2:
            self.checkBox.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
