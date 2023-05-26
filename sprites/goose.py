'''The main character.'''
from .sprite import Sprite
from PyQt6.QtCore import Qt
from numpy import pi, array
from .skeleton import Bone, Skeleton


class Goose(Sprite):
    def __init__(self):
        # duck colours
        self.body_col = '#FFFFFF'
        self.eyes_col = '#000000'
        self.beak_col = '#f3a200'
        self.feet_col = '#f3a200'

        # duck dimensions
        self.x = 100
        self.y = 200
        self.body_width = 40

        self.head_width = 20
        self.neck_width = self.head_width * 0.95

        self.eye_radius = 3
        self.eye_wonkiness = -pi/18  # small angle
        self.eye_distance = self.head_width * 0.9

        self.chin_size = 0.3
        self.beak_width = self.head_width*0.6

        self.foot_width = 6

        self.build()
        self.update()
        return

    def build(self):
        """Build a skeleton."""
        self.skeleton = Skeleton()
        self.upper_body = Bone(40 / 2., 0.)
        self.lower_body = Bone(self.upper_body.orientation / 2.,
                               self.upper_body.orientation + pi)
        self.neck = Bone(30., pi / 2.)
        self.head = Bone(10., 0.)
        self.feet = Bone(self.body_width * .6,
                         self.upper_body.orientation - pi/4.)

        # forehead attaching to end of head is jank
        # TODO: fix jank
        self.forehead = Bone(self.head.length * .8, -self.head.orientation)
        self.left_eye = Bone(self.eye_distance / 2.,
                             self.head.orientation + pi/2. + self.eye_wonkiness)
        self.right_eye = Bone(self.eye_distance / 2.,
                              self.head.orientation - pi/2. - self.eye_wonkiness)

        self.chin = Bone(self.head.length * .3, self.head.orientation + pi)
        self.beak = Bone(self.head.length * .5, self.head.orientation)

        self.skeleton.attach(self.lower_body)
        self.skeleton.attach(self.upper_body)
        self.skeleton.attach(self.feet)
        self.upper_body.attach(self.neck)
        self.neck.attach(self.head)
        self.head.attach(self.forehead)
        self.forehead.attach(self.left_eye)
        self.forehead.attach(self.right_eye)
        self.head.attach(self.chin)
        self.chin.attach(self.beak)

    def update(self):
        self.head.rotate(0.001)

        # calculate feet positions
        foot_offset = array([5, 0])
        self.left_foot = self.feet.position - foot_offset
        self.right_foot = self.feet.position + foot_offset
        return

    def paint(self, painter):
        painter.translate(self.x, self.y)

        # Draw the duck body
        painter.setPen(width=self.body_width, color=self.body_col,
                       capStyle=Qt.PenCapStyle.RoundCap)
        painter.drawLine(self.lower_body.position, self.upper_body.position)

        # Draw the duck neck
        painter.setPen(width=int(self.neck_width))
        painter.drawLine(self.upper_body.position, self.neck.position)

        # Draw the duck head
        painter.setPen(width=self.head_width)
        painter.drawLine(self.neck.position, self.head.position)

        # Draw the duck eyes
        painter.setPen(width=int(self.eye_radius*2), color=self.eyes_col)
        painter.drawPoints(self.left_eye.position, self.right_eye.position)

        # Draw the duck beak
        painter.setPen(width=int(self.beak_width), color=self.beak_col)
        painter.drawLine(self.chin.position, self.beak.position)

        # Draw the duck feet
        painter.setPen(width=self.foot_width, color=self.feet_col,
                       capStyle=Qt.PenCapStyle.SquareCap)
        painter.drawPoints(self.left_foot, self.right_foot)
