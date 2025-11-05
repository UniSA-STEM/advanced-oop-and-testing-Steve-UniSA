"""
File: staff.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from animal import Animal


class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__duties = []
        self.__assigned_animals = []

    def __get_name(self):
        return self.__name

    def __get_role(self):
        return self.__role

    def __get_duties(self):
        return self.__duties

    def get_assigned_animals(self):
        return self.__assigned_animals

    def __set_name(self, name):
        self.__name = name

    def __set_role(self, role):
        self.__role = role

    def add_duties(self, duty):
        self.__duties.append(duty)

    def remove_duties(self, duty):
        self.__duties.remove(duty)

    def add_assigned_animals(self, animal):
        self.__assigned_animals.append(animal)

    def remove_assigned_animals(self, animal):
        self.__assigned_animals.remove(animal)

    def feed_animal(self, animal: Animal):
        if self.__duties.__contains__("feed animal"):
            if self.__assigned_animals.__contains__(animal):
                # Feed the animal
                pass
        else:
            raise Exception(f"Sorry, your role is not assigned to feed {animal.name}")

    def clean_enclosure(self, animal: Animal):
        if self.__duties.__contains__("clean enclosure"):
            if self.__assigned_animals.__contains__(animal):
                # Clean the enclosure
                pass
        else:
            raise Exception(f"Sorry, your role is not assigned to clean enclosures for {animal.name}")

    def conduct_health_check(self, animal: Animal):
        if self.__duties.__contains__("conduct health check"):
            if self.__assigned_animals.__contains__(animal):
                # Conduct the health check
                pass
        else:
            raise Exception(f"Sorry, your role is not assigned to conduct health checks for {animal.name}")

    def __str__(self):
        return f"Name: {self.__name}\nRole: {self.__role}\nDuties: {self.__duties}"

    name = property(__get_name, __set_name)
    role = property(__get_role, __set_role)
    duties = property(__get_duties)
