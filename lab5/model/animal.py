'''from core import MapDirection, MoveDirection, Vector2d

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
'''