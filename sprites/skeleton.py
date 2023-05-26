"""Skeleton acts as a rig base for a Sprite."""
from numpy import pi, sin, cos, array


class Bone:
    def __init__(self, length: float, orientation: float):
        self.length = length
        self.orientation = orientation
        self.parent = None
        self.children = []
        return

    def __repr__(self):
        return f"Bone({self.length}, {self.orientation})"

    def attach(self, bone):
        if bone in self.children:
            raise Exception(f"{bone} is already attached to {self}.")
        bone.parent = self
        self.children.append(bone)
        return bone

    def rotate(self, angle: float):
        """Rotate bone and all attached bones."""
        self.orientation += angle
        self.orientation %= 2*pi
        for child in self.children:
            child.rotate(angle)

    @property
    def root_position(self):
        return self.parent.position

    @property
    def position(self):
        """Gets position of the end of the bone."""
        # using -sin because positive angle should correspond to up on screen
        return self.parent.position + self.length * array([cos(self.orientation), -sin(self.orientation)]) # noqa E501


class Skeleton:
    """Act as root for bones to attach to."""
    def __init__(self):
        self.position = array([0, 0])
        self.children = []

    def attach(self, bone):
        if bone in self.children:
            raise Exception("Bone is already attached to skeleton.")
        bone.parent = self
        self.children.append(bone)
