import sys

from PyQt5.Qt import Qt
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QButtonGroup, QDialog, QLabel, QRadioButton


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

        '''
        Radio Buttons gets the context from their parent so if
        you use only the radio button without grouping them, you can only
        have one group.

        To use multiple radio buttons in one parent widget, you have to
        use button group.

        Also helpful to get which radio button was checked on event handler.
        '''

        # Text Color Radio Buttons

        self.radioButtonGroupTextColor = QButtonGroup(self)

        self.radioButtonTextColorRed = QRadioButton("Red", self)
        self.radioButtonTextColorRed.move(100, 210)
        self.radioButtonTextColorRed.setChecked(True)
        self.radioButtonGroupTextColor.addButton(self.radioButtonTextColorRed)

        self.radioButtonTextColorBlue = QRadioButton("Blue", self)
        self.radioButtonTextColorBlue.move(100, 240)
        self.radioButtonGroupTextColor.addButton(self.radioButtonTextColorBlue)

        self.radioButtonTextColorGreen = QRadioButton("Green", self)
        self.radioButtonTextColorGreen.move(100, 270)
        self.radioButtonGroupTextColor.addButton(self.radioButtonTextColorGreen)

        # Text Font Size Radio Buttons

        self.radioButtonGroupFontSize = QButtonGroup(self)

        self.radioButtonFontSizeSmall = QRadioButton("Small", self)
        self.radioButtonFontSizeSmall.move(200, 210)
        self.radioButtonGroupFontSize.addButton(self.radioButtonFontSizeSmall)

        self.radioButtonFontSizeMedium = QRadioButton("Medium", self)
        self.radioButtonFontSizeMedium.move(200, 240)
        self.radioButtonFontSizeMedium.setChecked(True)
        self.radioButtonGroupFontSize.addButton(self.radioButtonFontSizeMedium)

        self.radioButtonFontSizeLarge = QRadioButton("Large", self)
        self.radioButtonFontSizeLarge.move(200, 270)
        self.radioButtonGroupFontSize.addButton(self.radioButtonFontSizeLarge)

        self.connect_signals()
        self.show()

    def connect_signals(self):

        # TODO : search for any better way to connect the signals

        # text color

        self.radioButtonTextColorRed.clicked.connect(self.eh_textColorRadioButtonClicked)
        self.radioButtonTextColorBlue.clicked.connect(self.eh_textColorRadioButtonClicked)
        self.radioButtonTextColorGreen.clicked.connect(self.eh_textColorRadioButtonClicked)

        # font size

        self.radioButtonFontSizeSmall.clicked.connect(self.eh_fontSizeRadioButtonClicked)
        self.radioButtonFontSizeMedium.clicked.connect(self.eh_fontSizeRadioButtonClicked)
        self.radioButtonFontSizeLarge.clicked.connect(self.eh_fontSizeRadioButtonClicked)

    def eh_textColorRadioButtonClicked(self):
        button = self.radioButtonGroupTextColor.checkedButton()
        self.__textLabelTextColor = button.text().lower()
        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.__textLabelBackgroundColor, self.__textLabelTextColor, self.__textLabelFontSize
            )
        )

    def eh_fontSizeRadioButtonClicked(self):
        sFontSize = self.radioButtonGroupFontSize.checkedButton().text()
        print(sFontSize)
        if sFontSize == "Small":
            self.__textLabelFontSize = 20
        elif sFontSize == "Medium":
            self.__textLabelFontSize = 40
        elif sFontSize == "Large":
            self.__textLabelFontSize = 60

        self.textLabel.setStyleSheet(
            self.__textLabelStyleTemplate.format(
                self.__textLabelBackgroundColor, self.__textLabelTextColor, self.__textLabelFontSize
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
