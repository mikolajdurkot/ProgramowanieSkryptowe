from typing import Dict
from core import Vector2d, MoveDirection
from interface import IMoveValidator, IWorldMap, Animal
from view import MapVisualizer



class RectangularMap(IMoveValidator, IWorldMap):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.animals: Dict[Vector2d, Animal] = {}

    def canMoveTo(self, position: Vector2d) -> bool:
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def place(self, animal: Animal) -> bool:
        if self.canMoveTo(animal.position) and animal.position not in self.animals:
            self.animals[animal.position] = animal
            return True
        return False

    def move(self, animal: Animal, direction: MoveDirection) -> None:
        new_position = animal.position

        if direction == MoveDirection.FORWARD:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            new_position -= animal.orientation.toUnitVector()

        if self.canMoveTo(new_position) and new_position not in self.animals:
            del self.animals[animal.position]
            animal.position = new_position
            self.animals[new_position] = animal

    def isOccupied(self, position: Vector2d) -> bool:
        return position in self.animals

    def objectAt(self, position: Vector2d) -> Animal or None:
        return self.animals.get(position, None)

    def __str__(self) -> str:
        visualizer = MapVisualizer(self)
        return visualizer.draw()
