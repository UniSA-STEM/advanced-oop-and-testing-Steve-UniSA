"""
File: enclosure.py
Description: This file contains the Enclosure class.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal, Bird, Mammal, Reptile


class Enclosure:
    def __init__(self, size: int, environment: str, cleanliness: str) -> None:
        """
        This class represents an enclosure. Enclosures have a size and environment.
        :param size:
        :param environment:
        :param cleanliness:
        """
        self.__size = size
        self.__environment = environment
        self.__cleanliness = cleanliness
        self.__animals = []

    def __get_size(self) -> int:
        """
        This method returns the size of the enclosure
        :return:
        """
        return self.__size

    def __get_environment(self) -> str:
        """
        This method returns the environment type of the enclosure.
        :return:
        """
        return self.__environment

    def __get_cleanliness(self) -> str:
        """
        This method returns the cleanliness of the enclosure.
        :return:
        """
        return self.__cleanliness

    def __get_animals(self):
        """
        This method returns the list animals in the enclosure.
        :return:
        """
        return self.__animals

    def __set_size(self, size) -> None:
        """
        This method updates the size of the enclosure.
        :param size:
        :return:
        """
        self.__size = size

    def __set_environment(self, environment: str) -> None:
        """
        This method updates the environment type of the enclosure.
        :param environment:
        :return:
        """
        self.__environment = environment

    def __set_cleanliness(self, cleanliness: str) -> None:
        """
        This method updates the cleanliness of the enclosure.
        :param cleanliness:
        :return:
        """
        self.__cleanliness = cleanliness

    def add_animal(self, animal: Animal) -> None:
        """
        This method adds animals to the enclosure.
        :param animal:
        :return:
        """
        if self.is_compatible(animal):
            self.animals.append(animal)
            animal.enclosure = self
        else:
            raise ValueError("Incompatible animal for this enclosure.")

    def remove_animal(self, animal) -> None:
        """
        This method removes animals from the enclosure.
        :param animal:
        :return:
        """
        # TODO: Remove animal from enclosure
        pass

    def status(self) -> str:
        """
        This method returns the status of the enclosure.
        :return:
        """
        self.__get_cleanliness()

    def clean_enclosure(self) -> None:
        """
        This method records a cleaning of the enclosure.
        :return:
        """
        # TODO: Implement clean_enclosure.
        pass

    def is_compatible(self, animal) -> bool:
        """
        This method checks whether the enclosure is compatible with the animal we would like to
        assign to the environment.
        :param animal:
        :return:
        """
        # TODO: Implement check to see if enclosure is compatible with animal.
        pass

    def __str__(self):
        """
        The string conversion method returns the enclosure environment.
        :return:
        """
        return f"Name: {self.__environment}"

    # Properties
    size = property(__get_size, __set_size)
    environment = property(__get_environment, __set_environment)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)
