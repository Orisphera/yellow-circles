import random
import sys
from PyQt5 import uic
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

MAX_X = MAX_Y = 400


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        size = random.randint(0, min(MAX_X, MAX_Y))
        rx, ly = random.randint(size, MAX_X), random.randint(size, MAX_Y)
        self.circles.append(QRect(QPoint(rx - size, ly - size), QPoint(rx, ly)))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setPen(QColor(255, 255, 0))
        for r in self.circles:
            qp.drawEllipse(r)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
