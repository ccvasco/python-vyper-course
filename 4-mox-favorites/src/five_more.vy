# pragma version 0.4.0
# @license MIT

import favorites
import second_module


initializes: favorites
exports: (
    favorites.retrieve,
    favorites.add_person
)

# initializes: second_module
# exports: (second_module.__interface__)

@deploy
def __init__():
    favorites.__init__()
    # second_module.__init__()

@external
def store(new_number: uint256):
    favorites.my_favorite_number = new_number + 5

# @external
# def call_second(input: bool):
#     second_module.set_to(input)
    


