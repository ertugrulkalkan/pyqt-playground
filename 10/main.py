import sys

from PyQt5.Qt import Qt
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QSpinBox, QLabel


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

        self.spinBox = QSpinBox(self)
        self.spinBox.resize(QSize(150, 30))
        self.spinBox.move(QPoint(175, 300))
        self.spinBox.setRange(20, 100)
        self.spinBox.setValue(self.__textLabelFontSize)
        self.spinBox.setSuffix(" px")

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.spinBox.valueChanged.connect(self.eh_spinBoxValueChanged)

    def eh_spinBoxValueChanged(self, value):
        self.__textLabelFontSize = value
        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.__textLabelBackgroundColor, self.__textLabelTextColor, self.__textLabelFontSize
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
