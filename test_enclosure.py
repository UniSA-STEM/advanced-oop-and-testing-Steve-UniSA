"""
File: test_enclosure.py
Description: This file contains the unit tests for the Enclosure class.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enclosure import Enclosure
from animal import Bird, Mammal, Reptile


# Check that enclosures can be correctly instantiated
def test_valid_enclosure_initialization():
    enclosure = Enclosure("Rainforest Habitat", "Medium", "Rainforest", 7)
    assert enclosure.name == "Rainforest Habitat"
    assert enclosure.size == "Medium"
    assert enclosure.environment == "Rainforest"
    assert enclosure.cleanliness == 7
    assert enclosure.id == 1
    assert enclosure.animals == []


# Check for invalid name data types
def test_invalid_name_type():
    with pytest.raises(TypeError):
        Enclosure(123, "Small", "Arctic", 5)


# Check for invalid size
def test_invalid_size_value():
    with pytest.raises(ValueError):
        Enclosure("Tiny Tank", "Tiny", "Aquatic", 5)


# Check for invalid environment
def test_invalid_environment_value():
    with pytest.raises(ValueError):
        Enclosure("Unknown Biome", "Small", "Volcano", 5)


# Check for invalid cleanliness levels
def test_invalid_cleanliness():
    with pytest.raises(ValueError):
        Enclosure("Savannah Zone", "Large", "Savannah", -1)
        Enclosure("Savannah Zone", "Large", "Savannah", 11)
    with pytest.raises(TypeError):
        Enclosure("Savannah Zone", "Large", "Savannah", "Dirty")


# Test the clean_enclosure method
def test_clean_enclosure_sets_cleanliness_to_10():
    enclosure = Enclosure("Koala Corner", "Medium", "Temperate Forest", 3)
    enclosure.clean_enclosure()
    assert enclosure.cleanliness == 10


# Test the enclosure compatibility evaluation method
def test_is_compatible_true():
    enclosure = Enclosure("Macaw Nest", "Small", "Rainforest", 6)
    bird = Bird("Rio", "Macaw", 2, "Herbivore")
    assert enclosure.is_compatible(bird)


def test_is_compatible_false_due_to_size():
    enclosure = Enclosure("Tiny Tropics", "Small", "Rainforest", 6)
    reptile = Reptile("Komodo", "Komodo Dragon", 5, "Carnivore")
    assert not enclosure.is_compatible(reptile)


def test_is_compatible_false_due_to_environment():
    enclosure = Enclosure("Arctic Dome", "Small", "Arctic", 6)
    bird = Bird("Rio", "Macaw", 2, "Herbivore")
    assert not enclosure.is_compatible(bird)


# Test adding and removing animals from the enclosure
def test_add_and_remove_animal():
    enclosure = Enclosure("Penguin Pool", "Small", "Arctic", 8)
    bird = Bird("Pingu", "Penguin", 3, "Carnivore")
    enclosure.add_animal(bird)
    assert bird in enclosure.animals
    enclosure.remove_animal(bird)
    assert bird not in enclosure.animals


# Test that adding an incompatible animal to an enclosure fails
def test_add_incompatible_animal_raises():
    enclosure = Enclosure("Rainforest Retreat", "Small", "Rainforest", 9)
    mammal = Mammal("Leo", "Lion", 4, "Carnivore")
    with pytest.raises(ValueError):
        enclosure.add_animal(mammal)


# Test the enclosure status
def test_enclosure_status():
    enclosure = Enclosure("Sloth Sanctuary", "Medium", "Temperate Forest", 4)
    assert enclosure.status() == "Sloth Sanctuary has a cleanliness score of 4 out of 10."


# Test string representation
def test_enclosure_str():
    enclosure = Enclosure("Iguana Island", "Medium", "Rainforest", 7)
    assert str(enclosure) == "Name: Iguana Island"
