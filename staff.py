"""
File: staff.py
Description: This file contains the Staff class and its subclasses.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod
from typing import List
from animal import Animal
from enclosure import Enclosure


class Staff(ABC):
    _last_staff_id: int = 0

    def __init__(self, name) -> None:
        """
        This class represents the universal staff of the zoo. Staff have a name, role, and duties.
        :param name:
        """
        self._staff_id: int = Staff._last_staff_id + 1
        Staff._last_staff_id += 1
        self._set_name(name)
        self._assigned_animals = []

    def _get_id(self) -> int:
        """
        This method returns the id of the staff member.
        :return: integer
        """
        return self._staff_id

    def _get_name(self) -> str:
        """
        This method returns the name of the staff member.
        :return: string
        """
        return self._name

    def _get_assigned_animals(self) -> List[Animal]:
        """
        This method returns the assigned animals for the staff member.
        :return: List[Animal]
        """
        return self._assigned_animals

    def _set_name(self, name) -> None:
        """
        This method updates the name of the staff member.
        :param name:
        :return: None
        """
        self.__name = name

    def add_assigned_animals(self, animal) -> None:
        """
        This method assigns animals to the staff member.
        :param animal:
        :return: None
        """
        self._assigned_animals.append(animal)

    def remove_assigned_animals(self, animal) -> None:
        """
        This method removes animals from the staff member.
        :param animal:
        :return: None
        """
        self._assigned_animals.remove(animal)

    def __str__(self):
        """
        The string conversion method returns the staff member's name, role and duties.
        :return: None
        """
        return f"Id: {self._staff_id} Name: {self._name} Role: {type(self).__name__}"

    # Properties
    id = property(_get_id)
    name = property(_get_name, _set_name)
    assigned_animals = property(_get_assigned_animals)


class Zookeeper(Staff):
    """
    This class represents the zookeeper staff of the zoo. Staff have a name, role, and duties.
    :param name:
    """

    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal: Animal) -> str:
        """
        This method records that an animal has been fed.
        :param animal:
        :return: string
        """
        if self._assigned_animals.__contains__(animal):
            # Feed the animal
            return f"{animal.name} has been fed."
        else:
            return f"Sorry, you are not assigned to {animal.name}"

    def clean_enclosure(self, enclosure: Enclosure) -> str:
        """
        This method records that an enclosure has been cleaned.
        :param enclosure:
        :return: string
        """
        if self._assigned_animals.__contains__(enclosure):
            # Clean the enclosure
            enclosure.clean_enclosure()
            return f"Enclosure cleaned."
        else:
            return f"Sorry, you are not assigned to {enclosure.name}"


class Veterinarian(Staff):
    """
    This class represents the veterinarian staff of the zoo. Staff have a name, role, and duties.
    :param name:
    """

    def __init__(self, name):
        super().__init__(name)

    def conduct_health_check(self, animal: Animal) -> str:
        """
        This method records that a health check has been conducted on the animal.
        :param animal:
        :return: string
        """
        if self._assigned_animals.__contains__(animal):
            # Conduct the health check
            return f"Health check performed on {animal.name}."
        else:
            return f"Sorry, you are not assigned to {animal.name}"
