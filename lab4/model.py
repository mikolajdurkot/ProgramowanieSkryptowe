from typing import Type
from collections import namedtuple
from enum import Enum

class Vector2d(namedtuple('Vector2d', 'x y')):
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        direction_symbols = ['↑', '→', '↓', '←']
        return direction_symbols[self.value]

    def next(self) -> 'MapDirection':
        next_direction = (self.value + 1) % 4
        return MapDirection(next_direction)

    def previous(self) -> 'MapDirection':
        previous_direction = (self.value - 1) % 4
        return MapDirection(previous_direction)

    def toUnitVector(self) -> Vector2d:
        if self is MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self is MapDirection.EAST:
            return Vector2d(1, 0)
        elif self is MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self is MapDirection.WEST:
            return Vector2d(-1, 0)

class MoveDirection(Enum):
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"({self.position.x},{self.position.y}) {self.orientation}"

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
