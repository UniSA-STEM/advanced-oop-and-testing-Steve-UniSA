import pytest
from staff import Zookeeper, Veterinarian
from animal import Bird, Mammal, Reptile
from enclosure import Enclosure

# Check that staff can be correctly instantiated
def test_staff_initialization():
    keeper = Zookeeper("Alice")
    vet = Veterinarian("Bob")
    assert keeper.name == "Alice"
    assert vet.name == "Bob"
    assert keeper.id == 1
    assert vet.id == 2
    assert keeper.assigned_animals == []

# Test assigning and remove animals from staff
def test_assign_and_remove_animals():
    keeper = Zookeeper("Charlie")
    bird = Bird("Polly", "Macaw", 2, "Herbivore")
    keeper.add_assigned_animals(bird)
    assert bird in keeper.assigned_animals
    keeper.remove_assigned_animals(bird)
    assert bird not in keeper.assigned_animals

# Test that a zookeeper can feed animals
def test_zookeeper_feed_animal():
    keeper = Zookeeper("Dana")
    bird = Bird("Flap", "Penguin", 3, "Carnivore")
    assert keeper.feed_animal(bird) == "Sorry, you are not assigned to Flap"
    keeper.add_assigned_animals(bird)
    assert keeper.feed_animal(bird) == "Flap has been fed."

# Test that a zookeeper can clean enclosures
def test_zookeeper_clean_enclosure():
    keeper = Zookeeper("Eli")
    enclosure = Enclosure("savannah1", "Large", "Savannah", 10)
    mammal = Mammal("Simba", "Lion", 6, "Carnivore")
    enclosure.add_animal(mammal)
    assert keeper.clean_enclosure(enclosure) == "Sorry, you are not assigned to savannah1"
    keeper.add_assigned_animals(mammal)
    assert keeper.clean_enclosure(enclosure) == "Enclosure cleaned."

# Check that a veterinarian can conduct health checks
def test_veterinarian_health_check():
    vet = Veterinarian("Fay")
    bird = Bird("Squawk", "Macaw", 1, "Herbivore")
    assert vet.conduct_health_check(bird) == "Sorry, you are not assigned to Squawk"
    vet.add_assigned_animals(bird)
    assert vet.conduct_health_check(bird) == "Health check performed on Squawk."

# Test string representation
def test_staff_str_representation():
    keeper = Zookeeper("Gina")
    assert str(keeper) == f"Id: {keeper.id} Name: Gina Role: Zookeeper"
    vet = Veterinarian("Hank")
    assert str(vet) == f"Id: {vet.id} Name: Hank Role: Veterinarian"
