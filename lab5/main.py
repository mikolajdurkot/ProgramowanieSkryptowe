import sys
from controller import Simulation, OptionsParser
from model.core import MoveDirection, Vector2d # Import bezwzględny

directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:]) 
positions: list[Vector2d] = [Vector2d(0,0), Vector2d(0,0)] # Pozycje początkowe dla zwierząt, odpowiednio, (2,2) oraz (3,4) 
simulation: Simulation = Simulation(directions, positions)
simulation.run()     