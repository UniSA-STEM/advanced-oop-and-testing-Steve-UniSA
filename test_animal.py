"""
File: test_animal.py
Description: This file contains the unit tests for the Animal class.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from animal import Bird, Mammal, Reptile


@pytest.fixture
def flamingo() -> Bird:
    """

    :return:
    """
    return Bird("Fiona", "Flamingo", 3, "Herbivore", "Healthy")


@pytest.fixture
def lion() -> Mammal:
    """

    :return:
    """
    return Mammal("Simba", "Lion", 6, "Carnivore", "Healthy")


@pytest.fixture
def cobra() -> Reptile:
    """

    :return:
    """
    return Reptile("Kaa", "King Cobra", 3, "Omnivore", "Healthy")


# Check that birds can be correctly instantiated
def test_valid_bird_initialization(flamingo):
    """

    :param flamingo:
    :return:
    """
    assert flamingo.name == "Fiona"
    assert flamingo.species == "Flamingo"
    assert flamingo.age == 3
    assert flamingo.diet == "Herbivore"
    assert flamingo.id == 1
    assert not flamingo.sleeping


# Check that mammals can be correctly instantiated
def test_valid_mammal_initialization(lion):
    """

    :param lion:
    :return:
    """
    assert lion.name == "Simba"
    assert lion.species == "Lion"
    assert lion.age == 6
    assert lion.diet == "Carnivore"
    assert lion.id == 2
    assert not lion.sleeping


# Check that reptiles can be correctly instantiated
def test_valid_reptile_initialization(cobra):
    """

    :param cobra:
    :return:
    """
    assert cobra.name == "Kaa"
    assert cobra.species == "King Cobra"
    assert cobra.age == 3
    assert cobra.diet == "Omnivore"
    assert cobra.id == 3
    assert not cobra.sleeping


# Check for invalid name data types
def test_invalid_name_type_raises():
    """

    :return:
    """
    with pytest.raises(TypeError):
        Bird(123, "Flamingo", 3, "Herbivore", "Healthy")
        Mammal(45.6, "Lion", 6, "Carnivore", "Healthy")
        Reptile(["Kaa"], "King Cobra", 3, "Omnivore", "Healthy")


def test_invalid_name_value_raises():
    """

    :return:
    """
    with pytest.raises(ValueError):
        Bird("Fiona!", "Flamingo", 3, "Herbivore", "Healthy")
        Mammal("Simba_1", "Lion", 6, "Carnivore", "Healthy")
        Reptile("Kaa_snake", "King Cobra", 3, "Omnivore", "Healthy")


# Check for invalid species data types
def test_invalid_species_raises():
    """

    :return:
    """
    with pytest.raises(ValueError):
        Bird("Fiona", 45.7, 3, "Herbivore", "Healthy")
        Mammal("Simba", {"Lion"}, 6, "Carnivore", "Healthy")
        Reptile("Kaa", 123, 3, "Omnivore", "Healthy")


# Check for invalid ages
def test_invalid_age_raises():
    """

    :return:
    """
    with pytest.raises(ValueError):
        Bird("Fiona", "Flamingo", -3, "Herbivore", "Healthy")
        Mammal("Simba", "Lion", 6.9, "Carnivore", "Healthy")
        Reptile("Kaa", "King Cobra", "five", "Omnivore", "Healthy")


# Check for invalid diets
def test_invalid_diet_raises():
    """

    :return:
    """
    with pytest.raises(TypeError):
        Bird("Fiona", "Flamingo", 3, 45.2, "Healthy")
        Mammal("Simba", "Lion", 6, 3, "Healthy")
        Reptile("Kaa", "King Cobra", 3, ["Herbivore", "Carnivore"], "Healthy")


# Test Sleep and Awake
def test_sleep_and_awake(lion):
    """

    :param lion:
    :return:
    """
    assert not lion.sleeping
    assert lion.sleep() == "Simba is sleeping."
    assert lion.sleeping
    assert lion.awake() == "Simba is awake."
    assert not lion.sleeping


# Test feeding behavior
def test_eat_behavior(cobra):
    """

    :param cobra:
    :return:
    """
    assert cobra.eat() == "Kaa does not require feeding at the moment."
    cobra._set_needs_feeding()
    assert cobra.eat() == "Kaa is a omnivore and eats both plants and meat."
    assert not cobra._needs_feeding


# Test sounds
def test_make_sound_bird(flamingo):
    """

    :param flamingo:
    :return:
    """
    assert flamingo.make_sound() == "Fiona chirps or squawks."


def test_make_sound_mammal(lion):
    """

    :param lion:
    :return:
    """
    assert lion.make_sound() == "Simba roars or growls."


def test_make_sound_reptile(cobra):
    """

    :param cobra:
    :return:
    """
    assert cobra.make_sound() == "Kaa hisses."


# Test string representation
def test_str_representation(flamingo, lion, cobra):
    """

    :param flamingo:
    :param lion:
    :param cobra:
    :return:
    """
    assert str(flamingo) == f"Id: {flamingo.id} Name: Fiona Species: Flamingo"
    assert str(lion) == f"Id: {lion.id} Name: Simba Species: Lion"
    assert str(cobra) == f"Id: {cobra.id} Name: Kaa Species: King Cobra"
