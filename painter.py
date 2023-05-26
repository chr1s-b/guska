"""Wrap QPainter in an easy-to-use interface."""
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import QPoint, Qt
from numpy import array


class Painter(QPainter):
    def __init__(self, *args, antialiasing=True, **kwargs):
        super().__init__(*args, **kwargs)
        super().setRenderHint(QPainter.RenderHint.Antialiasing, antialiasing)
        self.pen = QPen()
        super().setPen(self.pen)

    def _toQPoint(self, point):
        return QPoint(*map(int, point))

    def drawLine(self, point1: array, point2: array):
        return super().drawLine(self._toQPoint(point1), self._toQPoint(point2))

    def drawPoints(self, *points: list[array]):
        return super().drawPoints(*[self._toQPoint(point) for point in points])

    def setPen(self, width: int = None, color: str = None,
               capStyle: Qt.PenCapStyle = None):
        if width:
            self.pen.setWidth(width)
        if color:
            try:
                color = QColor(color)
                self.pen.setColor(color)
            except TypeError:
                raise TypeError(f"{color} is an invalid colour value.")
        if capStyle:
            self.pen.setCapStyle(capStyle)

        super().setPen(self.pen)
