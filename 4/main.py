import sys

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.openFileButton = QPushButton(self)
        self.openFileButton.setText("Open Text File")
        self.openFileButton.resize(QSize(150, 20))
        self.openFileButton.move(QPoint(175, 10))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.openFileButton.clicked.connect(self.eh_openFileButton_clicked)

    def eh_openFileButton_clicked(self):
        '''
        there are some options to select:
            getOpenFileName -> select an existing file
            getOpenFileNames -> select some existing file
            getSaveFileName -> select an existing or non-existing file
        '''
        fFile, sExt = QFileDialog.getOpenFileName(self, "Open File", ".", "TXT File (*.txt);;Any (*)")

        if not sExt == '':
            print(fFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
