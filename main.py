import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter

import sprites

TITLE = "guska"
WIDTH = 640
HEIGHT = 480


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('QMainWindow {background:transparent}')
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 400, 400)

        self.goose = sprites.Goose()
        return

    def paintEvent(self, qpaint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        self.goose.update()
        self.goose.paint(painter)

        painter.end()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
