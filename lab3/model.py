from enum import Enum
import controller

class MoveDirection(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class Vector2d:
    def __init__(self, x1, y1):
        self.__x = x1
        self.__y = y1

    def __str__(self):
        return f'({self.__x}, {self.__y})'
    
    def precedes(self, other_Vector2d):
        return self.__x <= other_Vector2d.x and self.__y <= other_Vector2d.y

    def follows(self, other_Vector2d):
        return self.__x >= other_Vector2d.x and self.__y >= other_Vector2d.y

    def add(self, other_Vector2d):
        new_x = self.__x + other_Vector2d.x
        new_y = self.__y + other_Vector2d.y
        return Vector2d(new_x, new_y)

    def subtract(self, other_Vector2d):
        new_x = self.__x - other_Vector2d.x
        new_y = self.__y - other_Vector2d.y
        return Vector2d(new_x, new_y)

    def upperRight(self, other_Vector2d):
        new_x = max(self.__x, other_Vector2d.x)
        new_y = max(self.__y, other_Vector2d.y)
        return Vector2d(new_x, new_y)

    def lowerLeft(self, other_Vector2d):
        new_x = min(self.__x, other_Vector2d.x)
        new_y = min(self.__y, other_Vector2d.y)
        return Vector2d(new_x, new_y)

    def opposite(self):
        new_x = -self.__x
        new_y = -self.__y
        return Vector2d(new_x, new_y)

    def __eq__(self, other_Vector2d):
        return self.__x == other_Vector2d.x and self.__y == other_Vector2d.y
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.getter
    def x(self):
        return self.__x
    @y.getter
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, value):
        self.__x = value
    @y.setter
    def y(self, value):
        self.__y = value
