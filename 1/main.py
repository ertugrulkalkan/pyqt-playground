import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QRect, QSize, Qt, QSequentialAnimationGroup, QRect


class DialogMain(QDialog):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.setWindowTitle("My Gui")
        self.setFixedSize(QSize(300, 300))

        self.magicButton = QPushButton(self)
        self.magicButton.setText("Make some magic")
        self.magicButton.resize(QSize(150, 20))
        self.magicButton.move(75, 130)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.resize(10, 10)
        self.frame.move(145, 200)

        self.textLabel = QLabel(self)
        self.textLabel.setText("")
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.resize(QSize(150, 20))
        self.textLabel.move(75, 100)

    def make_some_magic(self):
        self.count += 1
        self.textLabel.setText(f"tadaaa {self.count}")
        self.do_animation()

    def do_animation(self):
        l = QRect(145, 200, 10, 10)
        h = QRect(140, 195, 20, 20)

        anim_get_bigger = QPropertyAnimation(self.frame, b"geometry")
        anim_get_bigger.setStartValue(l)
        anim_get_bigger.setEndValue(h)
        anim_get_bigger.setDuration(100)

        anim_get_smaller = QPropertyAnimation(self.frame, b"geometry")
        anim_get_smaller.setStartValue(h)
        anim_get_smaller.setEndValue(l)
        anim_get_smaller.setDuration(100)

        self.animation = QSequentialAnimationGroup(self.frame)
        self.animation.addAnimation(anim_get_bigger)
        self.animation.addAnimation(anim_get_smaller)
        self.animation.start()

    def connect_signals(self):
        self.magicButton.clicked.connect(self.make_some_magic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogMain()

    dialog.connect_signals()
    dialog.show()

    sys.exit(app.exec())
