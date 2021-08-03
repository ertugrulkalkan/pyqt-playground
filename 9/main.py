import sys

from PyQt5.Qt import Qt
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.__textLabelStyleTemplate = "background: {}; color: {}; font-size: {}px"
        self.__textLabelBackgroundColor = "lightgrey"
        self.__textLabelTextColor = "red"
        self.__textLabelFontSize = 40

        self.textLabel = QLabel(self)
        self.textLabel.resize(QSize(400, 150))
        self.textLabel.move(QPoint(50, 50))
        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.__textLabelBackgroundColor, self.__textLabelTextColor, self.__textLabelFontSize
            )
        )
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.setText("Hello !")

        # Background Color

        self.lineEditBackgroundColor = QLineEdit(self)
        self.lineEditBackgroundColor.setPlaceholderText("background color")
        self.lineEditBackgroundColor.setText(self.__textLabelBackgroundColor)
        self.lineEditBackgroundColor.resize(QSize(200, 30))
        self.lineEditBackgroundColor.move(150, 250)
        self.lineEditBackgroundColor.setEchoMode(QLineEdit.Normal)

        # Text Color

        self.lineEditTextColor = QLineEdit(self)
        self.lineEditTextColor.setPlaceholderText("text color")
        self.lineEditTextColor.setText(self.__textLabelTextColor)
        self.lineEditTextColor.resize(QSize(200, 30))
        self.lineEditTextColor.move(150, 290)
        self.lineEditTextColor.setEchoMode(QLineEdit.Normal)

        # Font Size

        self.lineEditFontSize = QLineEdit(self)
        self.lineEditFontSize.setPlaceholderText("font size")
        self.lineEditFontSize.setText(f"{self.__textLabelFontSize}")
        self.lineEditFontSize.resize(QSize(200, 30))
        self.lineEditFontSize.move(150, 330)
        self.lineEditFontSize.setEchoMode(QLineEdit.Normal)
        self.lineEditFontSize.setMaxLength(2)

        # Set Button

        self.buttonAppyStyle = QPushButton("Set", self)
        self.buttonAppyStyle.resize(QSize(200, 30))
        self.buttonAppyStyle.move(QPoint(150, 370))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.lineEditFontSize.textChanged.connect(self.fontsize_validator)
        self.buttonAppyStyle.clicked.connect(self.applyStyle)

    def fontsize_validator(self, input):
        if len(input) > 1:
            if input[-1] not in [f"{x}" for x in range(0, 10)]:
                self.sender().setText(input[:-1])

    def applyStyle(self):
        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.lineEditBackgroundColor.text(), self.lineEditTextColor.text(), self.lineEditFontSize.text()
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
