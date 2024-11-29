import sys
from random import randint

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QWidget, QApplication

from UI import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.point = QPoint()
        self.radius = 0
        self.flag = False
        self.color = QColor('yellow')
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.point = QPoint(randint(0, self.width()), randint(0, self.height()))
        self.radius = randint(1, self.width() // 2)
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.flag = True
        self.update()

    def draw(self, qp: QPainter):
        qp.setPen(self.color)
        qp.drawEllipse(self.point, self.radius, self.radius)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication([])
    win = Circles()
    win.show()
    sys.exit(app.exec())
