import pytest
from animal import Bird, Mammal, Reptile, Animal

# Check that birds can be correctly instantiated
def test_valid_bird_initialization():
    bird = Bird("Fiona", "Flamingo", 3, "Herbivore")
    assert bird.name == "Fiona"
    assert bird.species == "Flamingo"
    assert bird.age == 3
    assert bird.diet == "Herbivore"
    assert bird.id == 1
    assert not bird.sleeping

# Check that mammals can be correctly instantiated
def test_valid_mammal_initialization():
    mammal = Mammal("Simba", "Lion", 6, "Carnivore")
    assert mammal.name == "Simba"
    assert mammal.species == "Lion"
    assert mammal.age == 6
    assert mammal.diet == "Carnivore"
    assert mammal.id == 2
    assert not mammal.sleeping

# Check that reptiles can be correctly instantiated
def test_valid_reptile_initialization():
    reptile = Reptile("Kaa", "King Cobra", 3, "Omnivore")
    assert reptile.name == "Kaa"
    assert reptile.species == "King Cobra"
    assert reptile.age == 3
    assert reptile.diet == "Omnivore"
    assert reptile.id == 3
    assert not reptile.sleeping

# Check for invalid name data types
def test_invalid_name_type_raises():
    with pytest.raises(TypeError):
        Bird(123, "Flamingo", 3, "Herbivore")
        Mammal(45.6, "Lion", 6, "Carnivore")
        Reptile(["Kaa"], "King Cobra", 3, "Omnivore")

def test_invalid_name_value_raises():
    with pytest.raises(ValueError):
        Bird("Fiona!", "Flamingo", 3, "Herbivore")
        Mammal("Simba_1", "Lion", 6, "Carnivore")
        Reptile("Kaa_snake", "King Cobra", 3, "Omnivore")

# Check for invalid species data types
def test_invalid_species_raises():
    with pytest.raises(ValueError):
        Bird("Fiona", 45.7, 3, "Herbivore")
        Mammal("Simba", {"Lion"}, 6, "Carnivore")
        Reptile("Kaa", 123, 3, "Omnivore")

# Check for invalid ages
def test_invalid_age_raises():
    with pytest.raises(ValueError):
        Bird("Fiona", "Flamingo", -3, "Herbivore")
        Mammal("Simba", "Lion", 6.9, "Carnivore")
        Reptile("Kaa", "King Cobra", "five", "Omnivore")

# Check for invalid diets
def test_invalid_diet_raises():
    with pytest.raises(TypeError):
        Bird("Fiona", "Flamingo", 3, 45.2)
        Mammal("Simba", "Lion", 6, 3)
        Reptile("Kaa", "King Cobra", 3, ["Herbivore", "Carnivore"])

# Test Sleep and Awake
def test_sleep_and_awake():
    mammal = Mammal("Ellie", "Elephant", 10, "Herbivore")
    assert not mammal.sleeping
    assert mammal.sleep() == "Ellie is sleeping."
    assert mammal.sleeping
    assert mammal.awake() == "Ellie is awake."
    assert not mammal.sleeping

# Test feeding behavior
def test_eat_behavior():
    reptile = Reptile("Iggy", "Green Iguana", 2, "Herbivore")
    assert reptile.eat() == "Iggy does not require feeding at the moment."
    reptile._set_needs_feeding()
    assert reptile.eat() == "Iggy is a herbivore and eats plants."
    assert not reptile._needs_feeding

# Test sounds
def test_make_sound_bird():
    bird = Bird("Squawk", "Macaw", 2, "Herbivore")
    assert bird.make_sound() == "Squawk chirps or squawks."

def test_make_sound_mammal():
    mammal = Mammal("Leo", "Lion", 5, "Carnivore")
    assert mammal.make_sound() == "Leo roars or growls."

def test_make_sound_reptile():
    reptile = Reptile("Slither", "King Cobra", 4, "Carnivore")
    assert reptile.make_sound() == "Slither hisses."

# Test string representation
def test_str_representation():
    bird = Bird("Flap", "Penguin", 1, "Carnivore")
    mammal = Mammal("Leo", "Lion", 5, "Carnivore")
    reptile = Reptile("Slither", "King Cobra", 4, "Carnivore")
    assert str(bird) == f"Id: {bird.id} Name: Flap Species: Penguin"
    assert str(mammal) == f"Id: {mammal.id} Name: Leo Species: Lion"
    assert str(reptile) == f"Id: {reptile.id} Name: Slither Species: King Cobra"

