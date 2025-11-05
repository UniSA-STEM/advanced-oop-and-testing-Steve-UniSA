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
        self._name = name
        self._species = species
        self._age = age
        self._dietary_requirements = dietary_requirements

    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def get_dietary_requirements(self):
        return self._dietary_requirements

    def set_name(self, name):
        self._name = name

    def set_species(self, species):
        self._species = species

    def set_age(self, age):
        self._age = age

    def set_dietary_requirements(self, dietary_requirements):
        self._dietary_requirements = dietary_requirements

    def make_sound(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def __str__(self):
        return f"Name: {self._name} Species: {self._species}"

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    dietary_requirements = property(get_dietary_requirements, set_dietary_requirements)


class Bird(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_requirements):
        super().__init__(name, species, age, dietary_requirements)
