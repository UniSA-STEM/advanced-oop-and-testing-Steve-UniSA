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

        :return:
        """
        return self.__size

    def __get_environment(self) -> str:
        """

        :return:
        """
        return self.__environment

    def __get_cleanliness(self) -> str:
        """

        :return:
        """
        return self.__cleanliness

    def __get_animals(self):
        """

        :return:
        """
        return self.__animals

    def __set_size(self, size) -> None:
        """

        :param size:
        :return:
        """
        self.__size = size

    def __set_environment(self, environment: str) -> None:
        """

        :param environment:
        :return:
        """
        self.__environment = environment

    def __set_cleanliness(self, cleanliness: str) -> None:
        """

        :param cleanliness:
        :return:
        """
        self.__cleanliness = cleanliness

    def add_animal(self, animal: Animal) -> None:
        """

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

        :param animal:
        :return:
        """
        # TODO: Remove animal from enclosure
        pass

    def status(self) -> str:
        """

        :return:
        """
        self.__get_cleanliness()

    def clean_enclosure(self) -> None:
        """

        :return:
        """
        # TODO: Implement clean_enclosure.
        pass

    def is_compatible(self, animal) -> bool:
        """

        :param animal:
        :return:
        """
        # TODO: Implement check to see if enclosure is compatible with animal.
        pass

    def __str__(self):
        """

        :return:
        """
        return f""

    # Properties
    size = property(__get_size, __set_size)
    environment = property(__get_environment, __set_environment)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)
