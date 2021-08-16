import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QInputDialog, QLabel


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.lblData = QLabel(self)
        self.lblData.resize(200, 30)
        self.lblData.move(150, 40)

        self.ecmbExample = QComboBox(self)
        self.ecmbExample.setEditable(True)
        self.ecmbExample.setDuplicatesEnabled(False)
        self.ecmbExample.resize(200, 30)
        self.ecmbExample.move(150, 80)

        self.ecmbExample.addItem("1", "One")
        self.ecmbExample.addItem("2", "Two")
        self.ecmbExample.addItem("3", "Three")
        self.ecmbExample.addItem("4", "Four")

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ecmbExample.currentIndexChanged.connect(self.eh_ecmbExampleCurrentIndexChanged)

    def eh_ecmbExampleCurrentIndexChanged(self, index):
        data = self.ecmbExample.itemData(index)
        if not data:
            sStr, bOk = QInputDialog.getText(
                self,
                "Add Text",
                f"Add text to {self.ecmbExample.itemText(index)}",
            )
            if bOk:
                self.ecmbExample.setItemData(index, sStr)
        self.lblData.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
