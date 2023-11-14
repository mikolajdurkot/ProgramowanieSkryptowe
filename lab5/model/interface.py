"""
Autor: Stanisław Polak
Data utworzenia: 02-11-2023
Data modyfikacji: 10-11-2023
Wersja: 1.0.1
Opis: Klasy abstrakcyjne do ćwicznia 5.
"""

from abc import ABC, abstractmethod
from core import Vector2d, MoveDirection, MapDirection

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"{self.orientation}"

    def __repr__(self) -> str:
        return str(self)

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection) -> None:
        if direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        elif direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
        elif direction == MoveDirection.FORWARD:
            new_position = self.position + self.orientation.toUnitVector()
            if Vector2d(0, 0) <= new_position <= Vector2d(4, 4):
                self.position = new_position
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position - self.orientation.toUnitVector()
            if Vector2d(0, 0) <= new_position <= Vector2d(4, 4):
                self.position = new_position

class IMoveValidator(ABC):
    @abstractmethod
    def canMoveTo(self, position: Vector2d) -> bool:
        """
        Indicate if any object can move to the given position.

        Parameters:
            position:Vector2d
                The position checked for the movement possibility.
        Returns:
            True if the object can move to that position.
        """
        pass


class IWorldMap(ABC):
    @abstractmethod
    def place(self, animal: Animal) -> bool:
        """
        Place a animal on the map.

        Parameters:
            animal:Animal
                The animal to place on the map.
        Returns:
            True if the animal was placed. The animal cannot be placed if the move is not valid.
        """
        pass

    @abstractmethod
    def move(self, animal: Animal, direction: MoveDirection) -> None:
        """
        Moves an animal (if it is present on the map) according to specified direction.
        If the move is not possible, this method has no effect.
        """
        pass

    @abstractmethod
    def isOccupied(self, position: Vector2d) -> bool:
        """
        Return true if given position on the map is occupied. Should not be
        confused with 'canMoveTo()' since there might be empty positions where the animal
        cannot move.

        Parameters:
            position
                Position to check.
         Returns:
            True if the position is occupied.
        """
        pass

    @abstractmethod
    def objectAt(self, position: Vector2d) -> Animal | None:
        """
        Return an animal at a given position.

        Parameters:
            position:Vector2d
                The position of the animal.
         Returns:
            Animal or None if the position is not occupied.
        """
        pass