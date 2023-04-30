""" Define a Sprite class. """
from abc import ABC, abstractmethod


class Sprite(ABC):
    def __init__(self):
        return

    @abstractmethod
    def update(self):
        """ Update position. """
        pass

    @abstractmethod
    def paint(self):
        pass
