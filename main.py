import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QColor
from numpy import sin, cos, pi

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

    def paintEvent(self, qpaint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        # duck colours
        body_col = '#FFFFFF'
        eyes_col = '#000000'
        beak_col = '#f3a200'
        feet_col = '#f3a200'

        # duck dimensions
        body_width = 40
        body_length = 60
        body_orientation = 8*pi/6
        body_x = 100
        body_y = 100

        head_width = 30
        head_length = 10
        head_orientation = 17*pi/12
        neck_orientation = -pi/20
        neck_stretch = 30

        eye_radius = 2
        forehead_size = head_length * 0.2

        eye_wonkiness = -pi/18  # small angle
        eye_distance = head_width * 0.6

        foot_width = 6
        leg_length = body_width * 0.6
        foot_left_offset = 0
        foot_left_height = leg_length
        foot_right_offset = -foot_width * 2
        foot_right_height = leg_length

        # calculate coordinates
        body_bottom = QPoint(int(body_x - sin(body_orientation) * body_length / 2),
                             int(body_y + cos(body_orientation) * body_length / 2))

        body_top = QPoint(int(body_x + sin(body_orientation) * body_length / 2),
                          int(body_y - cos(body_orientation) * body_length / 2))

        head_x = int(body_top.x() + neck_stretch * sin(neck_orientation))
        head_y = int(body_top.y() - neck_stretch * cos(neck_orientation))

        head_top = QPoint(head_x, head_y)
        head_bottom = QPoint(int(head_x + head_length * sin(head_orientation)),
                             int(head_y - head_length * cos(head_orientation)))

        eye_centre = QPoint(int(head_x + forehead_size * sin(head_orientation)),
                            int(head_y - forehead_size * cos(head_orientation)))

        left_eye = QPoint(int(eye_centre.x() + eye_distance / 2 * cos(head_orientation + eye_wonkiness)),
                          int(eye_centre.y() + eye_distance / 2 * sin(head_orientation + eye_wonkiness)))

        right_eye = QPoint(int(eye_centre.x() - eye_distance / 2 * cos(head_orientation + eye_wonkiness)),
                           int(eye_centre.y() - eye_distance / 2 * sin(head_orientation + eye_wonkiness)))

        beak_width = head_width*0.4
        beak_length = head_length * 0.9
        beak_start = head_bottom - (head_top - head_bottom) * 0.5
        beak_end = QPoint(int(beak_start.x() + beak_length * sin(head_orientation)),
                          int(beak_start.y() - beak_length * cos(head_orientation)))

        left_foot = QPoint(int(body_x - foot_left_height * cos(body_orientation) + foot_left_offset * sin(body_orientation)),
                           int(body_y - foot_left_height * sin(body_orientation) - foot_left_offset * cos(body_orientation)))
        right_foot = QPoint(int(body_x - foot_right_height * cos(body_orientation) + foot_right_offset * sin(body_orientation)),
                            int(body_y - foot_right_height * sin(body_orientation) - foot_right_offset * cos(body_orientation)))

        # Draw the duck body
        pen = QPen()
        pen.setWidth(body_width)
        pen.setColor(QColor(body_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(body_bottom, body_top)

        # Draw the duck head
        pen = QPen()
        pen.setWidth(head_width)
        pen.setColor(QColor(body_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(head_top, head_bottom)

        # Draw the duck eyes
        pen = QPen()
        pen.setWidth(int(eye_radius*2))
        pen.setColor(QColor(eyes_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawPoints(left_eye, right_eye)

        # Draw the duck beak
        pen = QPen()
        pen.setWidth(int(beak_width))
        pen.setColor(QColor(beak_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(beak_start, beak_end)

        # Draw the duck feet
        pen = QPen()
        pen.setWidth(int(foot_width))
        pen.setColor(QColor(feet_col))
        pen.setCapStyle(Qt.PenCapStyle.SquareCap)
        painter.setPen(pen)
        painter.drawPoints(left_foot, right_foot)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
