"""
File: staff.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal
from enclosure import Enclosure


class Staff:
    def __init__(self, name, role) -> None:
        """
        This class represents the universal staff of the zoo. Staff have a name, role, and duties.
        :param name:
        :param role:
        """
        self.__name = name
        self.__role = role
        self.__duties = []
        self.__assigned_animals = []

    def __get_name(self):
        """
        This method returns the name of the staff member.
        :return:
        """
        return self.__name

    def __get_role(self):
        """
        This method returns the role of the staff member.
        :return:
        """
        return self.__role

    def __get_duties(self):
        """
        This method returns the duties of the staff member.
        :return:
        """
        return self.__duties

    def get_assigned_animals(self):
        """
        This method returns the assigned animals for the staff member.
        :return:
        """
        return self.__assigned_animals

    def __set_name(self, name) -> None:
        """
        This method updates the name of the staff member.
        :param name:
        :return:
        """
        self.__name = name

    def __set_role(self, role) -> None:
        """
        This method updates the role of the staff member.
        :param role:
        :return:
        """
        self.__role = role

    def add_duties(self, duty) -> None:
        """
        This method adds the duties to the staff member.
        :param duty:
        :return:
        """
        self.__duties.append(duty)

    def remove_duties(self, duty) -> None:
        """
        This method removes the duties from the staff member.
        :param duty:
        :return:
        """
        self.__duties.remove(duty)

    def add_assigned_animals(self, animal) -> None:
        """
        This method assigns animals to the staff member.
        :param animal:
        :return:
        """
        self.__assigned_animals.append(animal)

    def remove_assigned_animals(self, animal) -> None:
        """
        This method removes animals from the staff member.
        :param animal:
        :return:
        """
        self.__assigned_animals.remove(animal)

    def __str__(self):
        """

        :return:
        """
        return f"Name: {self.__name}\nRole: {self.__role}\nDuties: {self.__duties}"

    # Properties
    name = property(__get_name, __set_name)
    role = property(__get_role, __set_role)
    duties = property(__get_duties)


class Zookeeper(Staff):
    """
    This class represents the zookeeper staff of the zoo. Staff have a name, role, and duties.
    :param name:
    :param role:
    """

    def __init__(self, name, role):
        super().__init__(name, role)

    def feed_animal(self, animal: Animal) -> None:
        """

        :param animal:
        :return:
        """
        if self.__duties.__contains__("feed animal"):
            if self.__assigned_animals.__contains__(animal):
                # Feed the animal
                pass
            else:
                raise Exception(f"Sorry, you are not assigned to {animal.name}")
        else:
            raise Exception(f"Sorry, your role is not assigned to feed {animal.name}")

    def clean_enclosure(self, enclosure: Enclosure) -> None:
        """

        :param enclosure:
        :return:
        """
        if self.__duties.__contains__("clean enclosure"):
            if self.__assigned_animals.__contains__(enclosure):
                # Clean the enclosure
                enclosure.clean_enclosure()
            else:
                raise Exception(f"Sorry, you are not assigned to {enclosure.name}")
        else:
            raise Exception(f"Sorry, your role is not assigned to clean {enclosure.name}")


class Veterinarian(Staff):
    """
    This class represents the veterinarian staff of the zoo. Staff have a name, role, and duties.
    :param name:
    :param role:
    """

    def __init__(self, name, role):
        super().__init__(name, role)

    def conduct_health_check(self, animal: Animal) -> None:
        """

        :param animal:
        :return:
        """
        if self.__duties.__contains__("conduct health check"):
            if self.__assigned_animals.__contains__(animal):
                # Conduct the health check
                return f"Health check performed on {animal.name}."
            else:
                raise Exception(f"Sorry, you are not assigned to {animal.name}")
        else:
            raise Exception(f"Sorry, your role is not assigned to conduct health checks for {animal.name}")
