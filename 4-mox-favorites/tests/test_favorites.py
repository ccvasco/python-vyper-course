def test_starting_values(favorites_contract):
    print(favorites_contract.retrieve())
    assert favorites_contract.retrieve() == 27

def test_can_change_values(favorites_contract):
    favorites_contract.store(42)
    assert favorites_contract.retrieve() == 42

def test_can_add_people(favorites_contract):
    #Arrange
    new_person = "Neves"
    favorite_number = 27

    #Act
    favorites_contract.add_person(new_person, favorite_number)

    #Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)