"""
File: main.py
Description: This file contains the main application code for the project.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Random is used to create test animals for the demonstration script.
import random

from animal import Bird, Mammal, Reptile, Animal
from staff import Zookeeper, Veterinarian, Staff
from enclosure import Enclosure
from reports import Reports

def create_animals():
    # Create birds
    name = ["Fiona", "Diego", "Percy"]
    species = ["Flamingo", "Macaw", "Penguin"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Bird.DIET_OPTIONS))
        print(Bird(animal_name, species[name.index(animal_name)], age, diet, "Healthy"))

    # Create mammals
    name = ["Simba", "Eleanor", "Kylie", "Stanley"]
    species = ["Lion", "Elephant", "Koala", "Sloth"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Mammal.DIET_OPTIONS))
        print(Mammal(animal_name, species[name.index(animal_name)], age, diet, "Healthy"))

    # Create reptiles
    name = ["Drake", "Izzy", "Kaa"]
    species = ["Komodo Dragon", "Green Iguana", "King Cobra"]
    for animal_name in name:
        age = random.randint(1, 25)
        diet = random.choice(list(Reptile.DIET_OPTIONS))
        print(Reptile(animal_name, species[name.index(animal_name)], age, diet, "Healthy"))

if __name__ == '__main__':
    print("-" * 42)
    print(f"Demonstration of the zoo management system")
    print("-" * 42)

    print("-" * 80)
    print(f"Creating staff ...")
    print(f"Creating zookeepers ...")
    for staff_name in ["Fred", "George"]:
        print(Zookeeper(staff_name))
    print(f"Creating veterinarians ...")
    for staff_name in ["Steve"]:
        print(Veterinarian(staff_name))

    print(f"\nCreating enclosures ...")
    # Create enclosures
    print(Enclosure("wetlands_1", "Small", "Wetlands", 10))
    print(Enclosure("rainforest_1", "Small", "Rainforest", 10))
    print(Enclosure("arctic_1", "Small", "Arctic", 10))
    print(Enclosure("savannah_1", "Large", "Savannah", 10))
    print(Enclosure("savannah_2", "Large", "Savannah", 10))
    print(Enclosure("temperate_forest_1", "Medium", "Temperate Forest", 10))
    print(Enclosure("temperate_forest_2", "Medium", "Temperate Forest", 10))
    print(Enclosure("rainforest_2", "Medium", "Rainforest", 10))
    print(Enclosure("rainforest_3", "Medium", "Rainforest", 10))
    print(Enclosure("rainforest_4", "Medium", "Rainforest", 10))

    print(f"\nCreating animals ...")
    create_animals()
    print("-" * 80)

    print(f"Assign animals to staff ...")
    veterinarian_steve = None
    zookeeper_fred = None
    zookeeper_george = None
    for staff_member in Staff.staff_list:
        if staff_member.name == "Steve" and type(staff_member).__name__=="Veterinarian":
            veterinarian_steve = staff_member
        elif staff_member.name == "Fred" and type(staff_member).__name__=="Zookeeper":
            zookeeper_fred = staff_member
        elif staff_member.name == "George" and type(staff_member).__name__=="Zookeeper":
            zookeeper_george = staff_member

    for new_animal in Animal.animal_list:
        veterinarian_steve.add_assigned_animals(new_animal)
        if new_animal.id <= 5:
            zookeeper_fred.add_assigned_animals(new_animal)
        else:
            zookeeper_george.add_assigned_animals(new_animal)

    print(f"Animals assigned to Steve the veterinarian ...")
    for assigned_animal in veterinarian_steve.assigned_animals:
        print(assigned_animal.name)

    print(f"\nAnimals assigned to Fred the zookeeper ...")
    for assigned_animal in zookeeper_fred.assigned_animals:
        print(assigned_animal.name)

    print(f"\nAnimals assigned to George the zookeeper ...")
    for assigned_animal in zookeeper_george.assigned_animals:
        print(assigned_animal.name)

    print("-" * 80)
    print(f"Assign animals to enclosures ...")
    print(f"List enclosure requirements for each animal ...")
    for new_animal in Animal.animal_list:
        print(f"{new_animal.name} the {new_animal.species} requires a "
              f"{Animal.ZOO_ANIMALS[new_animal.species][0].lower()} {Animal.ZOO_ANIMALS[new_animal.species][1].lower()} enclosure.")
        enclosure_assigned = False
        for enclosure in Enclosure.enclosure_list:
            if (enclosure.environment == Animal.ZOO_ANIMALS[new_animal.species][1]
                    and enclosure.size == Animal.ZOO_ANIMALS[new_animal.species][0]
                    and enclosure_assigned == False):
                if len(enclosure.animals) == 0:
                    enclosure.add_animal(new_animal)
                    print(f"{new_animal.name} the {new_animal.species} has been assigned to {enclosure.name}.")
                    enclosure_assigned = True
    print("-" * 80)

    print(f"Update animal health ...")
    for animal in Animal.animal_list:
        if animal.id == 1:
            animal.hungry()
        elif animal.id == 3:
            animal.health = "Unwell. Ate bad sardines."
            print(f"{animal.name}'s health status is {animal.health}")
        elif animal.id == 5:
            animal.hungry()
        elif animal.id == 6:
            animal.health = "Requires close supervision. Not eating sufficient leaves."
            print(f"{animal.name}'s health status is {animal.health}")
        elif animal.id == 9:
            animal.hungry()

    print(f"\nConduct health checks ...")
    for animal in Animal.animal_list:
        print(f"{veterinarian_steve.conduct_health_check(animal)}")
        if animal.needs_feeding:
            print(f"*** {animal.name} needs feeding")

    print(f"\nFeed the animals ...")
    for assigned_animal in zookeeper_fred.assigned_animals:
        if assigned_animal.needs_feeding:
            print(zookeeper_fred.feed_animal(assigned_animal))

    for assigned_animal in zookeeper_george.assigned_animals:
        if assigned_animal.needs_feeding:
            print(zookeeper_george.feed_animal(assigned_animal))

    print(f"\nClean the enclosures")
    for assigned_animal in zookeeper_fred.assigned_animals:
        for enclosure in Enclosure.enclosure_list:
            for enclosure_animal in enclosure.animals:
                if assigned_animal.id == enclosure_animal.id:
                    print(f"{zookeeper_fred.name}: {zookeeper_fred.clean_enclosure(enclosure)}")

    for assigned_animal in zookeeper_george.assigned_animals:
        for enclosure in Enclosure.enclosure_list:
            for enclosure_animal in enclosure.animals:
                if assigned_animal.id == enclosure_animal.id:
                    print(f"{zookeeper_george.name}: {zookeeper_george.clean_enclosure(enclosure)}")

    print("-" * 80)

    print(f"\nRecord whether an animal is awake of asleep ...")
    for animal in Animal.animal_list:
        if animal.id % 2 ==0:
            animal.sleep()
        if animal.sleeping:
            print(f"{animal.name} is sleeping.")
        else:
            print(f"{animal.name} is awake.")

    print("-" * 80)
    print(f"\nPrint reports ...")
    reports = Reports()
    print(reports.staff_report())
    print(reports.animal_report())
    print(reports.enclosure_report())
    print(reports.animal_health_report())









