import sys
from random import randint

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.w = self.width()
        self.h = self.height()

        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw(painter)
            painter.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, painter):
        painter: QPainter
        painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(0, min(self.w, self.h))
        painter.drawEllipse(randint(0, self.w), randint(0, self.h), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
