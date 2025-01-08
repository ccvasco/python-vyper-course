from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os
from encrypt_key import KEYSTORE_PATH
import getpass 
from eth_account import Account

load_dotenv()
MY_ADDRESS = os.getenv("MY_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")


def main():
    print("Let's read in the Vyper code and deploy it")
    with open("favorites.vy", "r") as favorites_file: # "r" stands for in read-only mode
        favorites_code = favorites_file.read() # reads the whole content of a file into a single variable
        compliation_details = compile_code(favorites_code, output_formats=["bytecode", "abi"])
        # print(compliation_details)

    w3 = Web3(Web3.HTTPProvider(RPC_URL)) # connects to node (anvil)

    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], abi=compliation_details["abi"]) # creates a contract-type variable
    # print(favorites_contract)
    # breakpoint() # creates python shell

    print("building the transaction...")
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = favorites_contract.constructor().build_transaction(
        {
            "nonce": nonce,
            "from": MY_ADDRESS,
            "gasPrice": w3.eth.gas_price
        }
    )
    print(transaction)
    private_key = decrypt_key()
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    print(signed_transaction)

    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"My TX hash is {tx_hash}")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


def decrypt_key() -> str:
    with open (KEYSTORE_PATH, "r") as fp:
        encrypted_account = fp.read()
        password = getpass.getpass("Enter your password: ") #password is "password"
        key = Account.decrypt(encrypted_account, password)
        print("Decrypted key!")
        return key


if __name__ == "__main__":
    main()
