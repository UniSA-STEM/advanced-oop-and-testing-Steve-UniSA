"""
File: animal.py
Description: This file contains the Animal class and its subclasses.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, diet: str) -> None:
        """
        This class represents a universal animal. Animals have a name, species, age and diet.
        :param name:
        :param species:
        :param age:
        :param diet:
        """
        self._name: str = name
        self._species: str = species
        self._age: int = age
        self._diet: str = diet

    def __get_name(self) -> str:
        """
        This method returns the name of the animal.
        :return name:
        """
        return self._name

    def __get_species(self) -> str:
        """
        This method returns the species of the animal.
        :return:
        """
        return self._species

    def __get_age(self) -> int:
        """
        This method returns the age of the animal.
        :return:
        """
        return self._age

    def __get_diet(self) -> str:
        """
        This method returns the diet of the animal.
        :return:
        """
        return self._diet

    def __set_name(self, name) -> None:
        """
        This method updates the name of the animal.
        :param name:
        :return:
        """
        if isinstance(name, str):
            self._name = name

    def __set_species(self, species) -> None:
        """
        This method updates the species of the animal.
        :param species:
        :return:
        """
        if isinstance(species, str):
            self._species = species

    def __set_age(self, age) -> None:
        """
        This method updates the age of the animal.
        :param age:
        :return:
        """
        if isinstance(age, int) & age > 0:
            self._age = age

    def __set_diet(self, diet) -> None:
        """
        This method updates the diet of the animal.
        :param diet:
        :return:
        """
        self._diet = diet

    @abstractmethod
    def make_sound(self):
        """
        This method defines the abstract method for the animal making a sound.
        :return:
        """
        ...

    def eat(self):
        """
        This method allows the system to record that the animal has eaten.
        :return:
        """
        diet_options = {"Herbivore": "plants", "Carnivore": "meat", "Omnivore": "both plants and meat"}
        return f"{self._name} is a {self._diet.lower()} and eats {diet_options[self._diet]}."

    def sleep(self):
        """
        This method allows the system to record that the animal has slept.
        :return:
        """
        return f"{self._name} is sleeping."

    def __str__(self):
        """
        The string conversion method returns the animal name and species.
        :return:
        """
        return f"Name: {self._name} Species: {self._species}"

    # Properties
    name = property(__get_name, __set_name)
    species = property(__get_species, __set_species)
    age = property(__get_age, __set_age)
    diet = property(__get_diet, __set_diet)


class Bird(Animal):
    def __init__(self, name, species, age, diet):
        """
        This class represents a bird animal. Animals have a name, species, age and diet.
        :param name:
        :param species:
        :param age:
        :param diet:
        """
        super().__init__(name, species, age, diet)

    def make_sound(self):
        """
        This method implements the method for the bird making a sound.
        :return:
        """
        return f"{self._name} chirps or squawks."


class Mammal(Animal):
    """
    This class represents a mammalian animal. Animals have a name, species, age and diet.
    :param name:
    :param species:
    :param age:
    :param diet:
    """

    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        """
        This method implements the method for the mammal making a sound.
        :return:
        """
        return f"{self._name} roars or growls."


class Reptile(Animal):
    """
    This class represents a reptilian animal. Animals have a name, species, age and diet.
    :param name:
    :param species:
    :param age:
    :param diet:
    """

    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        """
        This method implements the method for the reptile making a sound.
        :return:
        """
        return f"{self._name} hisses."
