"""
File: staff.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__duties = []

    def __get_name(self):
        return self.__name

    def __get_role(self):
        return self.__role

    def __get_duties(self):
        return self.__duties

    def __set_name(self, name):
        self.__name = name

    def __set_role(self, role):
        self.__role = role

    def add_duties(self, duties):
        self.__duties.append(duties)

    def remove_duties(self, duties):
        self.__duties.remove(duties)

    def feed_animal(self):
        pass

    def clean_enclosure(self):
        pass

    def conduct_health_check(self):
        pass

    def __str__(self):
        return f"Name: {self.__name}\nRole: {self.__role}\nDuties: {self.__duties}"

    name = property(__get_name, __set_name)
    role = property(__get_role, __set_role)
    duties = property(__get_duties)