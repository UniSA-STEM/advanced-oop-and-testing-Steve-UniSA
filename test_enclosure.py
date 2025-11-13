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
@pytest.fixture
def medium_rainforest_enclosure() -> Enclosure:
    """
    Fixture for medium rainforest enclosure
    :return:
    """
    return Enclosure("Rainforest Habitat", "Medium", "Rainforest", 7)


@pytest.fixture
def small_rainforest_enclosure() -> Enclosure:
    """
    Fixture for small rainforest enclosure
    :return:
    """
    return Enclosure("Macaw Nest", "Small", "Rainforest", 6)


@pytest.fixture
def arctic_enclosure() -> Enclosure:
    """
    Fixture for arctic enclosure
    :return:
    """
    return Enclosure("Arctic Dome", "Small", "Arctic", 6)


@pytest.fixture
def temperate_forest_enclosure() -> Enclosure:
    """
    Fixture for temperate forest enclosure
    :return:
    """
    return Enclosure("Sloth Sanctuary", "Medium", "Temperate Forest", 4)


@pytest.fixture
def bird() -> Bird:
    """
    Fixture for rainforest bird
    :return:
    """
    return Bird("Rio", "Macaw", 2, "Herbivore", "Healthy")


@pytest.fixture
def penguin() -> Bird:
    """
    Fixture for arctic penguin
    :return:
    """
    return Bird("Pingu", "Penguin", 3, "Carnivore", "Healthy")


@pytest.fixture
def reptile() -> Reptile:
    """
    Fixture for reptile
    :return:
    """
    return Reptile("Komodo", "Komodo Dragon", 5, "Carnivore", "Healthy")


@pytest.fixture
def lion() -> Mammal:
    """
    Fixture for lion
    :return:
    """
    return Mammal("Leo", "Lion", 4, "Carnivore", "Healthy")


def test_valid_enclosure_initialization(medium_rainforest_enclosure):
    """
    Test the initialisation of an enclosure
    :param medium_rainforest_enclosure:
    :return:
    """
    assert medium_rainforest_enclosure.name == "Rainforest Habitat"
    assert medium_rainforest_enclosure.size == "Medium"
    assert medium_rainforest_enclosure.environment == "Rainforest"
    assert medium_rainforest_enclosure.cleanliness == 7
    assert medium_rainforest_enclosure.id == 1
    assert medium_rainforest_enclosure.animals == []


# Check for invalid name data types
def test_invalid_name_type():
    """
    Test to check that an invalid name (integer) raises a type error. Name 123 is invalid.
    :return:
    """
    with pytest.raises(TypeError):
        Enclosure(123, "Small", "Arctic", 5)


# Check for invalid size
def test_invalid_size_value():
    """
    Test to check that an invalid size value raises a value error. Size "Tiny" is invalid.
    :return:
    """
    with pytest.raises(ValueError):
        Enclosure("Tiny Tank", "Tiny", "Aquatic", 5)


# Check for invalid environment
def test_invalid_environment_value():
    """
    Test to check that an invalid environment value raises a value error
    :return:
    """
    with pytest.raises(ValueError):
        Enclosure("Unknown Biome", "Small", "Volcano", 5)


# Check for invalid cleanliness levels
def test_invalid_cleanliness():
    """

    :return:
    """
    with pytest.raises(ValueError):
        Enclosure("Savannah Zone", "Large", "Savannah", -1)
        Enclosure("Savannah Zone", "Large", "Savannah", 11)
    with pytest.raises(TypeError):
        Enclosure("Savannah Zone", "Large", "Savannah", "Dirty")


# Test the clean_enclosure method
def test_clean_enclosure_sets_cleanliness_to_10(medium_rainforest_enclosure):
    """

    :param medium_rainforest_enclosure:
    :return:
    """
    medium_rainforest_enclosure.clean_enclosure()
    assert medium_rainforest_enclosure.cleanliness == 10


# Test the enclosure compatibility evaluation method
def test_is_compatible_true(small_rainforest_enclosure, bird):
    """

    :param small_rainforest_enclosure:
    :param bird:
    :return:
    """
    assert small_rainforest_enclosure.is_compatible(bird)


def test_is_compatible_false_due_to_size(small_rainforest_enclosure, reptile):
    """

    :param small_rainforest_enclosure:
    :param reptile:
    :return:
    """
    assert not small_rainforest_enclosure.is_compatible(reptile)


def test_is_compatible_false_due_to_environment(arctic_enclosure, bird):
    """

    :param arctic_enclosure:
    :param bird:
    :return:
    """
    assert not arctic_enclosure.is_compatible(bird)


# Test adding and removing animals from the enclosure
def test_add_and_remove_animal(arctic_enclosure, penguin):
    """

    :param arctic_enclosure:
    :param penguin:
    :return:
    """
    arctic_enclosure.add_animal(penguin)
    assert penguin in arctic_enclosure.animals
    arctic_enclosure.remove_animal(penguin)
    assert penguin not in arctic_enclosure.animals


# Test that adding an incompatible animal to an enclosure fails
def test_add_incompatible_animal_raises(small_rainforest_enclosure, lion):
    """

    :param small_rainforest_enclosure:
    :param lion:
    :return:
    """
    with pytest.raises(ValueError):
        small_rainforest_enclosure.add_animal(lion)


# Test the enclosure status
def test_enclosure_status(temperate_forest_enclosure):
    """

    :param temperate_forest_enclosure:
    :return:
    """
    assert temperate_forest_enclosure.status() == "Sloth Sanctuary has a cleanliness score of 4 out of 10."


# Test string representation
def test_enclosure_str(medium_rainforest_enclosure):
    """

    :param medium_rainforest_enclosure:
    :return:
    """
    assert str(medium_rainforest_enclosure) == "Name: Rainforest Habitat"
