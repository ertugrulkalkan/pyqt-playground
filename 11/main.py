import sys

from PyQt5.QtCore import QDateTime, QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDateTimeEdit, QDialog, QMessageBox, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        '''
        QTime -> hours
        QDate -> days
        QDateTime -> days & hours
        '''

        self.dateTimeEdit = QDateTimeEdit(QDateTime().currentDateTime(), self)
        self.dateTimeEdit.resize(QSize(150, 30))
        self.dateTimeEdit.move(QPoint(175, 50))
        self.dateTimeEdit.setCalendarPopup(True)

        self.buttonEditDone = QPushButton("Set", self)
        self.buttonEditDone.resize(QSize(150, 30))
        self.buttonEditDone.move(QPoint(175, 90))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.dateTimeEdit.dateTimeChanged.connect(self.eh_dateTimeEditDateTimeChanged)
        self.buttonEditDone.clicked.connect(self.eh_buttonEditDoneClicked)

    def eh_dateTimeEditDateTimeChanged(self, date):
        now = QDateTime().currentDateTime()
        if now.secsTo(date) <= 0:
            self.dateTimeEdit.setStyleSheet("color: red;")
        else:
            self.dateTimeEdit.setStyleSheet("color: black;")

    def eh_buttonEditDoneClicked(self):
        date = self.dateTimeEdit.dateTime()
        now = QDateTime().currentDateTime()
        if now.secsTo(date) <= 0:
            QMessageBox.critical(self, "Error", "You should select a different date", QMessageBox.Ok)
            self.dateTimeEdit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
