"""
Autor: Stanisław Polak
Data utworzenia: 22-10-2023
Data modyfikacji: 22-10-2023
Wersja: 1.0
Opis: Testy integracyjne klasy "Animal".
"""      

import pytest
from model.core import MapDirection, Vector2d, MoveDirection
from model.animal import Animal


@pytest.fixture
def animal():
    # Tutaj kod, który, w przypadku modułu 'unittest', umieścilibyśmy w metodzie 'setUp()'  
    yield Animal(Vector2d(2, 2))  # Dane, które mają być testowane
    # Tutaj kod, który, w przypadku modułu 'unittest', umieścilibyśmy w metodzie 'tearDown()'


def test_Animal_isAt(animal: Animal):
    assert animal.isAt(Vector2d(2, 2))
    
    
def test_Animal_print(animal: Animal):
    assert str(animal) == "(2,2) ↑"


def test_Animal_move_north(animal: Animal):
    assert 1==1
    assert 1==1
    


def test_Animal_move_south(animal: Animal):
    assert 1==1
    assert 1==1
    


def test_Animal_move_east(animal: Animal):
    assert 1==1
    assert 1==1
    


def test_Animal_move_west(animal: Animal):
    assert 1==1
    assert 1==1
    