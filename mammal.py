"""
File: mammal.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)
