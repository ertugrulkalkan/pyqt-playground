import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QLabel, QMessageBox


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        visible_texts = ["None", "aA", "bB", "cC", "dD", "eE"]
        items = ["", "A", "B", "C", "D", "E"]
        self.data = dict(zip(visible_texts, items))

        self.lblValue = QLabel(self)
        self.lblValue.resize(200, 30)
        self.lblValue.move(150, 20)
        self.lblValue.setText("highlight one to see")

        self.cmbSelectOne = QComboBox(self)
        self.cmbSelectOne.resize(200, 30)
        self.cmbSelectOne.move(150, 50)
        for k, v in self.data.items():
            self.cmbSelectOne.addItem(k, {"value": v, "type": "letter"})
        self.cmbSelectOne.insertSeparator(1)

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.cmbSelectOne.currentIndexChanged.connect(self.eh_cmbCurrentIndexChanged)
        self.cmbSelectOne.highlighted.connect(self.eh_cmbHighlighted)

    def eh_cmbCurrentIndexChanged(self, index):
        data = self.cmbSelectOne.itemData(index)
        if data["value"]:
            QMessageBox.information(self, "Selected", f"You selected {data['value']} !")
        else:
            QMessageBox.warning(self, "Error", "You didn't selected any")

    def eh_cmbHighlighted(self, index):
        data = self.cmbSelectOne.itemData(index)
        self.lblValue.setText(data["value"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
