import boa

def main():
    print("Let's read in the Vyper code and deploy it!")
    favorites_contract = boa.load("favorites.vy")

    starting_favorites_number = favorites_contract.retrieve()
    print(f"The starting favorite number is: {starting_favorites_number}")

    favorites_contract.store(5) # This sends a tx
    ending_favorites_number = favorites_contract.retrieve()
    print(f"The ending favorite number is: {ending_favorites_number}")

if __name__ == "__main__":
    main()