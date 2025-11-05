"""
File: enclosure.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Enclosure:
    def __init__(self, size, environmental_type, cleanliness_level):
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness_level = cleanliness_level

    def status(self):
        return self.__cleanliness_level

    def clean_enclosure(self):
        pass