from enum import Enum
from model import Vector2d, Animal
from typing import List

class MoveDirection(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class OptionsParser:
    @staticmethod
    def parse(args):
        valid_moves = {
            'f': MoveDirection.FORWARD,
            'b': MoveDirection.BACKWARD,
            'l': MoveDirection.LEFT,
            'r': MoveDirection.RIGHT,
        }
        parsed_args = []

        for arg in args:
            if arg in valid_moves:
                parsed_args.append(valid_moves[arg])

        return parsed_args

class Simulation:
    def __init__(self, directions: List[MoveDirection], positions: List[Vector2d]):
        self.directions = directions
        self.animals = [Animal(position) for position in positions]

    def run(self):
        num = len(self.animals)
        for a in range(len(self.directions)):
            direction = self.directions[a]
            print(direction)
            animal = self.animals[a%num]
            animal.move(MoveDirection.FORWARD)
            print(f'Zwierzę {a%num} : ({animal.position.x},{animal.position.y}) {animal.orientation}')
