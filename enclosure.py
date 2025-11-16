"""
File: enclosure.py
Description: This file contains the Enclosure class.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal, Bird, Mammal, Reptile
from typing import List


class Enclosure:
    # Track the highest enclosure ID
    _last_enclosure_id: int = 0
    # Track the list of enclosures created for reporting purposes
    enclosure_list: List[Enclosure] = []
    # List of valid enclosure sizes at this zoo
    ENCLOSURE_SIZE = {"Small", "Medium", "Large"}
    # List of valid enclosure environments at this zoo
    ENCLOSURE_ENVIRONMENT = {"Savannah", "Rainforest", "Desert", "Aquatic", "Arctic", "Temperate Forest", "Mountain",
                             "Wetlands"}

    def __init__(self, name: str, size: str, environment: str, cleanliness: int) -> None:
        """
        This class represents an enclosure. Enclosures have a size and environment.
        :param size:
        :param environment:
        :param cleanliness:
        """
        self.__set_name(name)
        self.__set_size(size)
        self.__set_environment(environment)
        # Cleanliness is a rating from 1 to 10. 10 is cleanest.
        self.__set_cleanliness(cleanliness)
        self.__suitable_for = []
        self.__animals = []
        self.__enclosure_id: int = Enclosure._last_enclosure_id + 1
        Enclosure._last_enclosure_id += 1
        self.enclosure_list.append(self)

    def __get_enclosure_id(self) -> int:
        """
        This method returns the name of the enclosure
        :return:
        """
        return self.__enclosure_id

    def __get_name(self) -> str:
        """
        This method returns the name of the enclosure
        :return:
        """
        return self.__name

    def __get_size(self) -> str:
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

    def __get_cleanliness(self) -> int:
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

    def __set_name(self, name: str) -> None:
        """
        This method updates the name of the enclosure.
        :param name:
        :return:
        """
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("The name must be a string.")

    def __set_size(self, size: str) -> None:
        """
        This method updates the size of the enclosure.
        :param size:
        :return:
        """
        if size in Enclosure.ENCLOSURE_SIZE:
            self.__size = size
        else:
            raise ValueError("The species must one of the animal enclosure sizes at the zoo.")

    def __set_environment(self, environment: str) -> None:
        """
        This method updates the environment type of the enclosure.
        :param environment:
        :return:
        """
        if environment in Enclosure.ENCLOSURE_ENVIRONMENT:
            self.__environment = environment
        else:
            raise ValueError("The environment must one of the animal enclosure environments at the zoo.")

    def __set_cleanliness(self, cleanliness: int) -> None:
        """
        This method updates the cleanliness of the enclosure.
        :param cleanliness:
        :return:
        """
        if isinstance(cleanliness, int):
            if cleanliness >= 0 and cleanliness <= 10:
                self.__cleanliness = cleanliness
            else:
                raise ValueError("The cleanliness value must be between 0 and 10.")
        else:
            raise TypeError("The cleanliness must an integer value between 0 and 10.")

    def add_animal(self, animal: Animal) -> None:
        """
        This method adds animals to the enclosure.
        :param animal:
        :return:
        """
        if self.is_compatible(animal):
            self.__animals.append(animal)
        else:
            raise ValueError("This animal is incompatible with this enclosure.")

    def remove_animal(self, animal) -> None:
        """
        This method removes animals from the enclosure.
        :param animal:
        :return:
        """
        self.__animals.remove(animal)

    def status(self) -> str:
        """
        This method returns the status of the enclosure.
        :return:
        """
        return f"{self.__name} has a cleanliness score of {self.__cleanliness} out of 10."

    def clean_enclosure(self) -> None:
        """
        This method records a cleaning of the enclosure.
        :return:
        """
        self.__cleanliness = 10

    def is_compatible(self, animal) -> bool:
        """
        This method checks whether the enclosure is compatible with the animal we would like to
        assign to the environment.
        :param animal:
        :return:
        """
        required_enclosure_size = Animal.ZOO_ANIMALS[animal.species][0]
        required_enclosure_environment = Animal.ZOO_ANIMALS[animal.species][1]
        if self.__environment == required_enclosure_environment:
            if self.__size == required_enclosure_size:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        """
        The string conversion method returns the enclosure environment.
        :return:
        """
        return f"Name: {self.__name} Environment: {self.__environment} Cleanliness: {self.__cleanliness}"

    # Properties
    id = property(__get_enclosure_id)
    name = property(__get_name, __set_name)
    size = property(__get_size, __set_size)
    environment = property(__get_environment, __set_environment)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)
