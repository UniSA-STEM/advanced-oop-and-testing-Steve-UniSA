"""
File: enclosure.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal, Bird, Mammal, Reptile

class Enclosure:
    def __init__(self, size, environment, cleanliness):
        self.__size = size
        self.__environment = environment
        self.__cleanliness = cleanliness
        self.__animals = []

    def __get_size(self):
        return self.__size

    def __get_environment(self):
        return self.__environment

    def __get_cleanliness(self):
        return self.__cleanliness

    def __get_animals(self):
        return self.__animals

    def __set_size(self, size):
        self.__size = size

    def __set_environment(self, environment):
        self.__environment = environment

    def __set_cleanliness(self, cleanliness):
        self.__cleanliness = cleanliness

    def add_animal(self, animal):
        if self.is_compatible(animal):
            self.animals.append(animal)
            animal.enclosure = self
        else:
            raise ValueError("Incompatible animal for this enclosure.")

    def remove_animal(self, animal):
        pass

    def status(self):
        self.__get_cleanliness()

    def clean_enclosure(self):
        pass

    def is_compatible(self, animal):
        pass

    def __str__(self):
        return f""

    size = property(__get_size, __set_size)
    environment = property(__get_environment, __set_environment)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)
