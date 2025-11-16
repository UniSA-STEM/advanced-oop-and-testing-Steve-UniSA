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
    Fixture for zookeeper
    :return:
    """
    return Zookeeper("Alice")

@pytest.fixture
def vet() -> Veterinarian:
    """
    Fixture for veterinarian
    :return:
    """
    return Veterinarian("Bob")

@pytest.fixture
def polly() -> Bird:
    """
    Create an instance of Bird (Polly the Macaw) as a fixture
    :return:
    """
    return Bird("Polly", "Macaw", 2, "Herbivore", "Healthy")

@pytest.fixture
def savannah_enclosure() -> Enclosure:
    """
    Fixture for large savannah enclosure
    :return:
    """
    return Enclosure("savannah1", "Large", "Savannah", 10)

@pytest.fixture
def lion() -> Mammal:
    """
    Create an instance of Mammal (Simba the lion) as a fixture
    :return:
    """
    return Mammal("Simba", "Lion", 6, "Carnivore", "Healthy")

def test_staff_initialization(keeper, vet):
    """
    Check that staff can be correctly instantiated
    :param keeper:
    :param vet:
    :return:
    """
    assert keeper.name == "Alice"
    assert vet.name == "Bob"
    assert keeper.id == 1
    assert vet.id == 2
    assert keeper.assigned_animals == []


def test_assign_and_remove_animals(keeper, polly):
    """
    Test assigning and remove animals from staff
    :param keeper:
    :param polly:
    :return:
    """
    keeper.add_assigned_animals(polly)
    assert polly in keeper.assigned_animals
    keeper.remove_assigned_animals(polly)
    assert polly not in keeper.assigned_animals


def test_zookeeper_feed_animal(keeper, polly):
    """
    Test that a zookeeper can feed animals that are assigned to them
    :param keeper:
    :param polly:
    :return:
    """
    assert keeper.feed_animal(polly) == "Sorry, you are not assigned to Polly"
    keeper.add_assigned_animals(polly)
    assert keeper.feed_animal(polly) == "Polly has been fed."


def test_zookeeper_clean_enclosure(keeper, savannah_enclosure, lion):
    """
    Test that a zookeeper can clean enclosures assigned to them
    :param keeper:
    :param savannah_enclosure:
    :param lion:
    :return:
    """
    savannah_enclosure.add_animal(lion)
    assert keeper.clean_enclosure(savannah_enclosure) == "Sorry, you are not assigned to savannah1"
    keeper.add_assigned_animals(lion)
    assert keeper.clean_enclosure(savannah_enclosure) == "Enclosure cleaned."


def test_veterinarian_health_check(vet, polly):
    """
    Check that a veterinarian can conduct health checks assigned to them
    :param vet:
    :param polly:
    :return:
    """
    assert vet.conduct_health_check(polly) == "Sorry, you are not assigned to Polly"
    vet.add_assigned_animals(polly)
    assert vet.conduct_health_check(polly) == "Health check performed on Polly. Polly Macaw is Healthy."


def test_staff_str_representation(keeper, vet):
    """
    Check the output of the string representation for a zookeeper
    :param keeper:
    :param vet:
    :return:
    """
    assert str(keeper) == f"Id: {keeper.id} Name: Alice Role: Zookeeper"
    assert str(vet) == f"Id: {vet.id} Name: Bob Role: Veterinarian"
