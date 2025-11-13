"""
File: animal.py
Description: This file contains the Animal class and its subclasses.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    # Track the highest animal ID
    _last_animal_id: int = 0
    animal_list: List[Animal] = []
    # List of diet types
    DIET_OPTIONS = {"Herbivore": "plants", "Carnivore": "meat", "Omnivore": "both plants and meat"}
    # List of animals kept at this zoo
    # Stored as <Name>:[<Enclosure size>, <Enclosure environment>]
    ZOO_ANIMALS = {"Flamingo": ["Small", "Wetlands"], "Macaw": ["Small", "Rainforest"], "Penguin": ["Small", "Arctic"],
                   "Lion": ["Large", "Savannah"], "Elephant": ["Large", "Savannah"],
                   "Koala": ["Medium", "Temperate Forest"],
                   "Sloth": ["Medium", "Temperate Forest"], "Komodo Dragon": ["Medium", "Rainforest"],
                   "Green Iguana": ["Medium", "Rainforest"], "King Cobra": ["Medium", "Rainforest"]}

    def __init__(self, name: str, species: str, age: int, diet: str, health: str) -> None:
        """
        This class represents a universal animal. Animals have a name, species, age and diet.
        :param name:
        :param species:
        :param age:
        :param diet:
        """
        self._set_name(name)
        self._set_species(species)
        self._set_age(age)
        self._set_diet(diet)
        self._set_health(health)
        self._needs_feeding: bool = False
        self._sleeping: bool = False
        self._animal_id: int = Animal._last_animal_id + 1
        Animal._last_animal_id += 1
        self.animal_list.append(self)

    def _get_animal_id(self) -> int:
        """
        This method returns the id of the animal.
        :return id:
        """
        return self._animal_id

    def _get_name(self) -> str:
        """
        This method returns the name of the animal.
        :return name:
        """
        return self._name

    def _get_species(self) -> str:
        """
        This method returns the species of the animal.
        :return species:
        """
        return self._species

    def _get_age(self) -> int:
        """
        This method returns the age of the animal.
        :return age:
        """
        return self._age

    def _get_diet(self) -> str:
        """
        This method returns the diet of the animal.
        :return diet:
        """
        return self._diet

    def _get_sleeping(self) -> bool:
        """
        This method returns the sleeping state of the animal.
        :return sleeping state:
        """
        return self._sleeping

    def _get_health(self) -> str:
        return self._health

    def _set_name(self, name: str) -> None:
        """
        This method updates the name of the animal.
        :param name:
        :return:
        """
        if isinstance(name, str):
            if name.isalpha():
                self._name = name
            else:
                raise ValueError("The name must be a string using only alphabetical characters.")
        else:
            raise TypeError("The name must be a string.")

    def _set_species(self, species) -> None:
        """
        This method updates the species of the animal.
        :param species:
        :return:
        """
        if species in Animal.ZOO_ANIMALS:
            self._species = species
        else:
            raise ValueError("The species must one of the animal species kept at the zoo.")

    def _set_age(self, age) -> None:
        """
        This method updates the age of the animal.
        :param age:
        :return:
        """
        if isinstance(age, int):
            if age > 0:
                self._age = age
            else:
                raise ValueError("The age must be a positive integer value.")
        else:
            raise TypeError("The age must be an integer value.")

    def _set_diet(self, diet: str) -> None:
        """
        This method updates the diet of the animal.
        :param diet:
        :return:
        """
        if isinstance(diet, str):
            if diet.isalpha():
                self._diet = diet
            else:
                raise ValueError("The name must be a string using only alphabetical characters.")
        else:
            raise TypeError("The name must be a string.")

    def _set_health(self, health: str) -> None:
        """
        This method updates the health status of the animal.
        :param health:
        :return:
        """
        self._health = health

    def _set_needs_feeding(self) -> None:
        """
        This method marks the animal as requiring feeding.
        :param:
        :return:
        """
        self._needs_feeding = True

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
        if self._needs_feeding:
            self._needs_feeding = False
            return f"{self._name} is a {self._diet.lower()} and eats {Animal.DIET_OPTIONS[self._diet]}."
        else:
            return f"{self._name} does not require feeding at the moment."

    def sleep(self):
        """
        This method allows the system to record that the animal has slept.
        :return:
        """
        self._sleeping = True
        return f"{self._name} is sleeping."

    def awake(self):
        """
        This method allows the system to record that the animal has slept.
        :return:
        """
        self._sleeping = False
        return f"{self._name} is awake."

    def __str__(self):
        """
        The string conversion method returns the animal name and species.
        :return:
        """
        return f"Id: {self._animal_id} Name: {self._name} Species: {self._species}"

    # Properties
    id = property(_get_animal_id)
    name = property(_get_name, _set_name)
    species = property(_get_species, _set_species)
    age = property(_get_age, _set_age)
    diet = property(_get_diet, _set_diet)
    health = property(_get_health, _set_health)
    sleeping = property(_get_sleeping)


class Bird(Animal):
    def __init__(self, name, species, age, diet, health):
        """
        This class represents a bird animal. Animals have a name, species, age and diet.
        :param name:
        :param species:
        :param age:
        :param diet:
        """
        super().__init__(name, species, age, diet, health)

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

    def __init__(self, name, species, age, diet, health):
        super().__init__(name, species, age, diet, health)

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

    def __init__(self, name, species, age, diet, health):
        super().__init__(name, species, age, diet, health)

    def make_sound(self):
        """
        This method implements the method for the reptile making a sound.
        :return:
        """
        return f"{self._name} hisses."
