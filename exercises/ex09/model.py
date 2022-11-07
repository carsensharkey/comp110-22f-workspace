"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730560667"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, another_point: Point) -> float:
        """Returns the distance between two points."""
        x: float = self.x - another_point.x
        y: float = self.y - another_point.y
        return sqrt(x ** 2 + y ** 2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() is True:
            return "red"
        elif self.is_immune() is True:
            return "green"
        else:
            return "gray"

    def tick(self) -> None:
        """Reassign to the object's location attribute the result of adding the self object's loaction with its direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Reassign the sickness attribute to the INFECTED constant when a cell becomes infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determine whether or not a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Determine whether or not a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def immunize(self) -> None:
        """Assigns the IMMUNE constant to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Determines whether or not a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def contact_with(self, another_cell: Cell) -> None:
        """To be called when two Cell objects make contact."""
        if self.is_infected() is True and another_cell.is_vulnerable() is True:
            another_cell.contract_disease()
        elif self.is_vulnerable() is True and another_cell.is_infected() is True:
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, number_infected: int, number_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            if (number_infected + number_immune) >= cells or number_infected <= 0 or number_immune < 0:
                raise ValueError("Improper number of immune or infected cells in the call to model's constructor.")
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if len(self.population) < number_immune:
                cell.immunize()
                self.population.append(cell)
            elif len(self.population) < (number_infected + number_immune):
                cell.contract_disease()
                self.population.append(cell)
            else:
                self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Test whether any two Cell values come in contact with one another."""
        already_clashed: list = []
        for cell1 in self.population:
            for cell2 in self.population:
                if cell1 != cell2 and cell1 not in already_clashed:
                    if cell1.location.distance(cell2.location) < constants.CELL_RADIUS:
                        cell1.contact_with(cell2)
                        already_clashed.append(cell1)
                        already_clashed.append(cell2)

    def is_complete(self) -> bool:
        """Complete the simulation."""
        for cell in self.population:
            if cell.sickness > 0:
                return False
        return True

            