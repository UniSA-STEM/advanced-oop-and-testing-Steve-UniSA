"""
File: animal.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, species, age, diet):
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet

    def __get_name(self):
        return self._name

    def __get_species(self):
        return self._species

    def __get_age(self):
        return self._age

    def __get_diet(self):
        return self._diet

    def __set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def __set_species(self, species):
        if isinstance(species, str):
            self._species = species

    def __set_age(self, age):
        if isinstance(age, int) & age > 0 and age < 400:
            self._age = age

    def __set_diet(self, diet):
        self._diet = diet

    @abstractmethod
    def make_sound(self):
        ...

    def eat(self):
        diet_options = {"Herbivore": "plants", "Carnivore": "meat", "Omnivore": "both plants and meat"}
        return f"{self._name} is a {self._diet.lower()} and eats {diet_options[self._diet]}."

    def sleep(self):
        return f"{self._name} is sleeping."

    def __str__(self):
        return f"Name: {self._name} Species: {self._species}"

    name = property(__get_name, __set_name)
    species = property(__get_species, __set_species)
    age = property(__get_age, __set_age)
    diet = property(__get_diet, __set_diet)


class Bird(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        return f"{self._name} chirps or squawks."


class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        return f"{self._name} roars or growls."


class Reptile(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        return f"{self._name} hisses."
