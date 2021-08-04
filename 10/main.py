import sys

from PyQt5.Qt import Qt
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QDoubleSpinBox, QLabel, QSpinBox


def rgb2hex(r, g, b):
    return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.__textLabelStyleTemplate = "background: {}; color: {}; font-size: {}px"
        self.__textLabelBackgroundColor = "lightgrey"
        self.__textLabelTextColorR = 255
        self.__textLabelTextColorG = 255
        self.__textLabelTextColorB = 255
        self.__textLabelFontSize = 40

        # Test Text Label

        self.textLabel = QLabel(self)
        self.textLabel.resize(QSize(400, 150))
        self.textLabel.move(QPoint(50, 50))
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.setText("Hello !")

        self.applyStyle()

        # Font Size

        self.spinBoxFontSize = QSpinBox(self)
        self.spinBoxFontSize.resize(QSize(150, 30))
        self.spinBoxFontSize.move(QPoint(175, 300))
        self.spinBoxFontSize.setRange(20, 100)
        self.spinBoxFontSize.setValue(self.__textLabelFontSize)
        self.spinBoxFontSize.setSuffix(" px")

        # RED

        self.doubleSpinBoxR = QDoubleSpinBox(self)
        self.doubleSpinBoxR.resize(QSize(150, 30))
        self.doubleSpinBoxR.move(QPoint(175, 340))
        self.doubleSpinBoxR.setRange(0.0, 100.0)
        self.doubleSpinBoxR.setValue(100.0)
        self.doubleSpinBoxR.setSingleStep(0.5)
        self.doubleSpinBoxR.setSuffix(" %")
        self.doubleSpinBoxR.setDecimals(1)

        # GREEN

        self.doubleSpinBoxG = QDoubleSpinBox(self)
        self.doubleSpinBoxG.resize(QSize(150, 30))
        self.doubleSpinBoxG.move(QPoint(175, 380))
        self.doubleSpinBoxG.setRange(0.0, 100.0)
        self.doubleSpinBoxG.setValue(100.0)
        self.doubleSpinBoxG.setSingleStep(0.5)
        self.doubleSpinBoxG.setSuffix(" %")
        self.doubleSpinBoxG.setDecimals(1)

        # BLUE

        self.doubleSpinBoxB = QDoubleSpinBox(self)
        self.doubleSpinBoxB.resize(QSize(150, 30))
        self.doubleSpinBoxB.move(QPoint(175, 420))
        self.doubleSpinBoxB.setRange(0.0, 100.0)
        self.doubleSpinBoxB.setValue(100.0)
        self.doubleSpinBoxB.setSingleStep(0.5)
        self.doubleSpinBoxB.setSuffix(" %")
        self.doubleSpinBoxB.setDecimals(1)

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.spinBoxFontSize.valueChanged.connect(self.eh_spinBoxFontSizeValueChanged)
        self.doubleSpinBoxR.valueChanged.connect(self.eh_spinBoxRValueChanged)
        self.doubleSpinBoxG.valueChanged.connect(self.eh_spinBoxGValueChanged)
        self.doubleSpinBoxB.valueChanged.connect(self.eh_spinBoxBValueChanged)

    def eh_spinBoxFontSizeValueChanged(self, value):
        self.__textLabelFontSize = value
        self.applyStyle()

    def eh_spinBoxRValueChanged(self, value):
        self.__textLabelTextColorR = int((value / 100) * 255)
        self.applyStyle()

    def eh_spinBoxGValueChanged(self, value):
        self.__textLabelTextColorG = int((value / 100) * 255)
        self.applyStyle()

    def eh_spinBoxBValueChanged(self, value):
        self.__textLabelTextColorB = int((value / 100) * 255)
        self.applyStyle()

    def applyStyle(self):
        self.__textLabelTextColor = rgb2hex(
            self.__textLabelTextColorR, self.__textLabelTextColorG, self.__textLabelTextColorB
        )
        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.__textLabelBackgroundColor, self.__textLabelTextColor, self.__textLabelFontSize
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
