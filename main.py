"""
File: main.py
Description: This file contains the main application code for the project.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

from animal import Bird, Mammal, Reptile
from staff import Zookeeper, Veterinarian
from enclosure import Enclosure


def create_zoo():
    diet_options = ["Herbivore", "Carnivore", "Omnivore"]

    # Create birds
    name = ["Fiona", "Diego", "Percy"]
    species = ["Flamingo", "Macaw", "Penguin"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Bird.DIET_OPTIONS))
        new_animal = Bird(animal_name, species[name.index(animal_name)], age, diet)
        zoo_animals.append(new_animal)

    # Create mammals
    name = ["Simba", "Eleanor", "Kylie", "Stanley"]
    species = ["Lion", "Elephant", "Koala", "Sloth"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Mammal.DIET_OPTIONS))
        new_animal = Mammal(animal_name, species[name.index(animal_name)], age, diet)
        zoo_animals.append(new_animal)

    # Create reptiles
    name = ["Drake", "Izzy", "Kaa"]
    species = ["Komodo Dragon", "Green Iguana", "King Cobra"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Reptile.DIET_OPTIONS))
        new_animal = Reptile(animal_name, species[name.index(animal_name)], age, diet)
        zoo_animals.append(new_animal)

    for new_animal in zoo_animals:
        veterinarian_steve.add_assigned_animals(new_animal)
        if new_animal.id <= 5:
            zookeeper_fred.add_assigned_animals(new_animal)
        else:
            zookeeper_george.add_assigned_animals(new_animal)


if __name__ == '__main__':
    try:
        Reptile("animal_name", "species[name.index(animal_name)]", 10, "herbivore")
    except Exception as ex:
        print (f"{ex}\n")

    # Create staff
    zookeeper_fred = Zookeeper("Fred")
    zookeeper_george = Zookeeper("George")
    veterinarian_steve = Veterinarian("Steve")

    zoo_animals = []
    create_zoo()

    for animal in zoo_animals:
        print(animal)
        print(animal.make_sound())
        print(animal.sleep())
        print(animal.eat())

    print(f"\nAnimals assigned to veterinarian Steve:")
    for animal in veterinarian_steve.assigned_animals:
        print(animal)

    print(f"\nAnimals assigned to zookeeper Fred:")
    for animal in zookeeper_fred.assigned_animals:
        print(animal)

    print(f"\nAnimals assigned to zookeeper George:")
    for animal in zookeeper_george.assigned_animals:
        print(animal)

    # Find animal id 6
    for animal in zoo_animals:
        if animal.id == 6:
            print(f"\n{veterinarian_steve.conduct_health_check(animal)}")
        if animal.id == 7:
            print(f"\n{zookeeper_fred.feed_animal(animal)}")
            print(f"\n{zookeeper_george.feed_animal(animal)}")
        if animal.id == 8:
            print(f"\n{animal.sleep()}")
