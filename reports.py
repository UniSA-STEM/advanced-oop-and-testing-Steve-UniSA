"""
File: reports.py
Description: This file contains the reports for the solution.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from staff import Staff
from animal import Animal
from enclosure import Enclosure


class Reports:
    def staff_report(self) -> str:
        """
        Produce a report of the staff working at the zoo
        :return:
        """
        report = "Current staff list\n"
        report += "-" * 35 + "\n"
        for staff_member in Staff.staff_list:
            report += f"{'{:<5}'.format(str(staff_member.id))}{'{:<15}'.format(str(staff_member.name))}{'{:>15}'.format(str(type(staff_member).__name__))}\n"
        report += "-" * 35 + "\n"
        return report

    def animal_report(self) -> str:
        """
        Create a report of the animals at the zoo
        :return:
        """
        report = "Current animal list\n"
        report += "-" * 50 + "\n"
        for animal in Animal.animal_list:
            report += f"{'{:<5}'.format(str(animal.id))}{'{:<15}'.format(animal.name)}{'{:>15}'.format(animal.species)}\n"
        return report

    def enclosure_report(self) -> str:
        """
        Create a report of the enclosures at the zoo
        :return:
        """
        report = "Current enclosure list\n"
        report += "-" * 50 + "\n"
        for enclosure in Enclosure.enclosure_list:
            report += f"{'{:<5}'.format(str(enclosure.id))}{'{:<15}'.format(enclosure.name)}{'{:>15}'.format(enclosure.environment)}\n"
        return report

    def animal_health_report(self) -> str:
        """
        Create a health report of the animals at the zoo
        :return:
        """
        report = "Current animal health list\n"
        report += "-" * 65 + "\n"
        for animal in Animal.animal_list:
            report += f"{'{:<5}'.format(str(animal.id))}{'{:<15}'.format(animal.name)}{'{:>15}'.format(animal.species)}{'{:>15}'.format(animal.species)}{'{:>15}'.format(animal.health)}\n"
        report += "-" * 65 + "\n"
        return report