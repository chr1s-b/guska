"""Helper functions."""
from PyQt6.QtCore import QPoint


def toQPoint(point):
    """Convert point to QPoint."""
    return QPoint(*map(int, point))
