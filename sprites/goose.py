'''The main character.'''
from .sprite import Sprite
from numpy import sin, cos, pi
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPen, QColor


class Goose(Sprite):
    def __init__(self):
        # duck colours
        self.body_col = '#FFFFFF'
        self.eyes_col = '#000000'
        self.beak_col = '#f3a200'
        self.feet_col = '#f3a200'

        # duck dimensions
        self.body_width = 40
        self.body_length = 40
        self.body_orientation = 8*pi/6
        self.body_x = 100
        self.body_y = 100

        self.head_width = 20
        self.head_length = 10
        self.head_orientation = 17*pi/12
        self.neck_orientation = -pi/5
        self.neck_stretch = 30
        self.neck_width = self.head_width * 0.95

        self.eye_radius = 3
        self.forehead_size = self.head_length * 0.6
        self.eye_wonkiness = -pi/18  # small angle
        self.eye_distance = self.head_width * 0.9

        self.chin_size = 0.3
        self.beak_width = self.head_width*0.6
        self.beak_length = self.head_length * 0.5

        self.foot_width = 6
        self.leg_length = self.body_width * 0.6
        self.foot_left_offset = 0
        self.foot_left_height = self.leg_length
        self.foot_right_offset = -self.foot_width * 2
        self.foot_right_height = self.leg_length
        return

    def update(self):
        # calculate coordinates
        self.body_bottom = QPoint(int(self.body_x - sin(self.body_orientation)*self.body_length/2),
                                  int(self.body_y + cos(self.body_orientation)*self.body_length/2))

        self.body_top = QPoint(int(self.body_x + sin(self.body_orientation)*self.body_length/2),
                               int(self.body_y - cos(self.body_orientation)*self.body_length/2))

        head_x = int(self.body_top.x() + self.neck_stretch * sin(self.neck_orientation))
        head_y = int(self.body_top.y() - self.neck_stretch * cos(self.neck_orientation))

        self.head_top = QPoint(head_x, head_y)
        self.head_bottom = QPoint(int(head_x + self.head_length * sin(self.head_orientation)),
                                  int(head_y - self.head_length * cos(self.head_orientation)))

        eye_centre_x = head_x + self.forehead_size * sin(self.head_orientation)
        eye_centre_y = head_y - self.forehead_size * cos(self.head_orientation)

        self.left_eye = QPoint(int(eye_centre_x + self.eye_distance / 2 * cos(self.head_orientation + self.eye_wonkiness)),
                               int(eye_centre_y + self.eye_distance / 2 * sin(self.head_orientation + self.eye_wonkiness)))

        self.right_eye = QPoint(int(eye_centre_x - self.eye_distance / 2 * cos(self.head_orientation + self.eye_wonkiness)),
                                int(eye_centre_y - self.eye_distance / 2 * sin(self.head_orientation + self.eye_wonkiness)))

        self.beak_start = self.head_bottom - (self.head_top - self.head_bottom)*self.chin_size
        self.beak_end = QPoint(int(self.beak_start.x() + self.beak_length * sin(self.head_orientation)),
                               int(self.beak_start.y() - self.beak_length * cos(self.head_orientation)))

        self.left_foot = QPoint(int(self.body_x - self.foot_left_height * cos(self.body_orientation) + self.foot_left_offset * sin(self.body_orientation)),
                                int(self.body_y - self.foot_left_height * sin(self.body_orientation) - self.foot_left_offset * cos(self.body_orientation)))
        self.right_foot = QPoint(int(self.body_x - self.foot_right_height * cos(self.body_orientation) + self.foot_right_offset * sin(self.body_orientation)),
                                 int(self.body_y - self.foot_right_height * sin(self.body_orientation) - self.foot_right_offset * cos(self.body_orientation)))

    def paint(self, painter):
        # Draw the duck body
        pen = QPen()
        pen.setWidth(self.body_width)
        pen.setColor(QColor(self.body_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(self.body_bottom, self.body_top)

        # Draw the duck neck
        pen = QPen()
        pen.setWidth(int(self.neck_width))
        pen.setColor(QColor(self.body_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(self.body_top, self.head_top)

        # Draw the duck head
        pen = QPen()
        pen.setWidth(self.head_width)
        pen.setColor(QColor(self.body_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(self.head_top, self.head_bottom)

        # Draw the duck eyes
        pen = QPen()
        pen.setWidth(int(self.eye_radius*2))
        pen.setColor(QColor(self.eyes_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawPoints(self.left_eye, self.right_eye)

        # Draw the duck beak
        pen = QPen()
        pen.setWidth(int(self.beak_width))
        pen.setColor(QColor(self.beak_col))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawLine(self.beak_start, self.beak_end)

        # Draw the duck feet
        pen = QPen()
        pen.setWidth(int(self.foot_width))
        pen.setColor(QColor(self.feet_col))
        pen.setCapStyle(Qt.PenCapStyle.SquareCap)
        painter.setPen(pen)
        painter.drawPoints(self.left_foot, self.right_foot)
