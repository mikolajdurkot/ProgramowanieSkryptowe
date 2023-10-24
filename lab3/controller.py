from enum import Enum

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

    @staticmethod
    def run(move_directions):
        move_descriptions = {
            MoveDirection.FORWARD: 'Zwierzak idzie do przodu',
            MoveDirection.BACKWARD: 'Zwierzak idzie do tyłu',
            MoveDirection.LEFT: 'Zwierzak skręca w lewo',
            MoveDirection.RIGHT: 'Zwierzak skręca w prawo',
        }
        output = []

        for move in move_directions:
            if move in move_descriptions:
                output.append(move_descriptions[move])

        return output
