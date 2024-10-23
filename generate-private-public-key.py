import secrets
from web3 import Web3

def generate_keys():
    '''Generates ethereum public and private key with options to save to file and print
    '''

    # Generate a new private key
    private_key = '0x' + secrets.token_hex(32)
    web3 = Web3()

    account = web3.eth.account.from_key(private_key)
    public_key = account.address

    save_to_file = input(
        "Do you want to save the keys to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        with open('private.txt', 'w', encoding='utf-8') as f:
            f.write(f"Private Key: {private_key}\n")
            f.write(f"Public Address: {public_key}\n")
        print("Keys have been saved to private.txt")

    print_to_terminal = input(
        "Do you want to print the keys to the terminal? (yes/no): ").strip().lower()
    if print_to_terminal == 'yes':
        print(f"Private Key: {private_key}")
        print(f"Public Address: {public_key}")


if __name__ == "__main__":
    generate_keys()
