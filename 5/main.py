import sys

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(500, 500))

        self.actionButton = QPushButton("Action", self)
        self.actionButton.resize(QSize(150, 25))
        self.actionButton.move(QPoint(175, 50))

        self.__text_to_print = """
        <h1>LOREM IPSUM</h1>
        <p>Lorem ipsum dolor sit amet,<br>
        consectetur adipiscing elit. Maecenas<br>
        libero mauris, efficitur sit amet<br>
        dolor in, tempus maximus risus. Integer.</p>
        """
        self.pixmapLabel = QLabel(self)
        self.pixmapLabel.setText(self.__text_to_print)
        self.pixmapLabel.resize(QSize(400, 350))
        self.pixmapLabel.move(75, 100)

        QFontDatabase.addApplicationFont("./5/JetBrainsMono[wght].ttf")
        self.pixmapLabel.setFont(QFont("JetBrains Mono"))

        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.actionButton.clicked.connect(self.eh_actionButton)

    def eh_actionButton(self):
        self.pxm = QPixmap("./5/logo.png")
        self.pixmapLabel.setPixmap(self.pxm.scaled(QSize(350, 350), 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    sys.exit(app.exec())
