"""
File: animal.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Animal:
    def __init__(self, name, species, age, dietary_requirements):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_requirements = dietary_requirements

    def speak(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def __str__(self):
        print(f"Name: {self.__name}")

class Mammal(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)

class Reptile(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)

class Bird(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)
