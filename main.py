"""
File: main.py
Description: This file contains the main application code for the project.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

from animal import Animal, Bird, Mammal, Reptile
from staff import Staff


def create_zoo():
    diet_options = ["Herbivore", "Carnivore", "Omnivore"]

    # Create birds
    name = ["Fiona", "Diego", "Percy"]
    species = ["Flamingo", "Macaw", "Penguin"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(diet_options)
        zoo_animals.append(Bird(animal_name, species[name.index(animal_name)], age, diet))

    # Create mammals
    name = ["Simba", "Eleanor", "Kylie", "Stanley"]
    species = ["Lion", "Elephant", "Koala", "Sloth"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(diet_options)
        zoo_animals.append(Mammal(animal_name, species[name.index(animal_name)], age, diet))

    # Create reptiles
    name = ["Drake", "Izzy", "Kaa"]
    species = ["Komodo Dragon", "Green Iguana", "King Cobra"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(diet_options)
        zoo_animals.append(Reptile(animal_name, species[name.index(animal_name)], age, diet))


if __name__ == '__main__':
    zoo_animals = []
    create_zoo()

    for animal in zoo_animals:
        print(animal)
        print(animal.id)
        print(animal.make_sound())
        print(animal.sleep())
        print(animal.eat())
