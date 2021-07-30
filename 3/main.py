import sys

from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QLabel, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.nameLabel = QLabel(self)
        self.nameLabel.move(QPoint(150, 240))
        self.nameLabel.setFixedSize(QSize(200, 20))
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameLabel.setText("John Doe")

        self.changeNameButton = QPushButton("Change Name", self)
        self.changeNameButton.resize(QSize(200, 20))
        self.changeNameButton.move(QPoint(150, 270))

        self.ageLabel = QLabel(self)
        self.ageLabel.move(QPoint(150, 300))
        self.ageLabel.setFixedSize(QSize(200, 20))
        self.ageLabel.setAlignment(Qt.AlignCenter)
        self.ageLabel.setText(f"{40}")

        self.changeAgeButton = QPushButton("Change Age", self)
        self.changeAgeButton.resize(QSize(200, 20))
        self.changeAgeButton.move(QPoint(150, 330))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.changeNameButton.clicked.connect(self.eh_changeNameButton_clicked)
        self.changeAgeButton.clicked.connect(self.eh_changeAgeButton_clicked)

    def eh_changeNameButton_clicked(self):
        sName, bOK = QInputDialog.getText(self, "Name", "Enter Your Name:", text=self.nameLabel.text())

        if bOK:
            self.nameLabel.setText(sName)

    def eh_changeAgeButton_clicked(self):
        iAge, bOK = QInputDialog.getInt(
            self, "Age", "Enter Your Age:", value=int(self.ageLabel.text()), min=5, max=120, step=1
        )

        if bOK:
            self.ageLabel.setText(f"{iAge}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
