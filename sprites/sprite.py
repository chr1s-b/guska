""" Define a Sprite class. """
from abc import ABC, abstractmethod


class Sprite(ABC):
    @abstractmethod
    def build(self):
        """Create a Skeleton."""
        return

    @abstractmethod
    def update(self):
        """Update position."""
        pass

    @abstractmethod
    def paint(self):
        """Draw Sprite."""
        pass
