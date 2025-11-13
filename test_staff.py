"""
File: test_staff.py
Description: This file contains the unit tests for the Staff class.
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import pytest

from staff import Zookeeper, Veterinarian
from animal import Bird, Mammal, Reptile
from enclosure import Enclosure

@pytest.fixture
def keeper() -> Zookeeper:
    """

    :return:
    """
    return Zookeeper("Alice")

@pytest.fixture
def vet() -> Veterinarian:
    """

    :return:
    """
    return Veterinarian("Bob")

@pytest.fixture
def polly() -> Bird:
    """

    :return:
    """
    return Bird("Polly", "Macaw", 2, "Herbivore", "Healthy")

@pytest.fixture
def savannah_enclosure() -> Enclosure:
    """

    :return:
    """
    return Enclosure("savannah1", "Large", "Savannah", 10)

@pytest.fixture
def lion() -> Mammal:
    """

    :return:
    """
    return Mammal("Simba", "Lion", 6, "Carnivore", "Healthy")

# Check that staff can be correctly instantiated
def test_staff_initialization(keeper, vet):
    """

    :param keeper:
    :param vet:
    :return:
    """
    assert keeper.name == "Alice"
    assert vet.name == "Bob"
    assert keeper.id == 1
    assert vet.id == 2
    assert keeper.assigned_animals == []


# Test assigning and remove animals from staff
def test_assign_and_remove_animals(keeper, polly):
    """

    :param keeper:
    :param polly:
    :return:
    """
    keeper.add_assigned_animals(polly)
    assert polly in keeper.assigned_animals
    keeper.remove_assigned_animals(polly)
    assert polly not in keeper.assigned_animals


# Test that a zookeeper can feed animals
def test_zookeeper_feed_animal(keeper, polly):
    """

    :param keeper:
    :param polly:
    :return:
    """
    assert keeper.feed_animal(polly) == "Sorry, you are not assigned to Polly"
    keeper.add_assigned_animals(polly)
    assert keeper.feed_animal(polly) == "Polly has been fed."


# Test that a zookeeper can clean enclosures
def test_zookeeper_clean_enclosure(keeper, savannah_enclosure, lion):
    """

    :param keeper:
    :param savannah_enclosure:
    :param lion:
    :return:
    """
    savannah_enclosure.add_animal(lion)
    assert keeper.clean_enclosure(savannah_enclosure) == "Sorry, you are not assigned to savannah1"
    keeper.add_assigned_animals(lion)
    assert keeper.clean_enclosure(savannah_enclosure) == "Enclosure cleaned."


# Check that a veterinarian can conduct health checks
def test_veterinarian_health_check(vet, polly):
    """

    :param vet:
    :param polly:
    :return:
    """
    assert vet.conduct_health_check(polly) == "Sorry, you are not assigned to Polly"
    vet.add_assigned_animals(polly)
    assert vet.conduct_health_check(polly) == "Health check performed on Polly. Polly Macaw is Healthy."


# Test string representation
def test_staff_str_representation(keeper, vet):
    """

    :param keeper:
    :param vet:
    :return:
    """
    assert str(keeper) == f"Id: {keeper.id} Name: Alice Role: Zookeeper"
    assert str(vet) == f"Id: {vet.id} Name: Bob Role: Veterinarian"
