from web3 import Web3
import sys


def send_eth(recipient: str, amount: float, private_key: str):
    # Connect to an Ethereum node (e.g., Infura)
    rpc_url = "https://eth.llamarpc.com"
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Check if connected
    if not web3.is_connected():
        print("Failed to connect to Ethereum network")
        return

    recipient_checksum = web3.to_checksum_address(recipient)

    # Get the sender address from the private key
    account = web3.eth.account.from_key(private_key)
    sender = account.address

    # Create the transaction
    nonce = web3.eth.get_transaction_count(sender)
    gas_price = web3.eth.gas_price
    value = web3.to_wei(amount, 'ether')

    tx = {
        'nonce': nonce,
        'to': recipient_checksum,
        'value': value,
        'gas': 21000,
        'gasPrice': gas_price,
        'chainId': 1  # Mainnet chain ID
    }

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Transaction hash: {web3.to_hex(tx_hash)}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Missing arguments: send-eth-to-address.py <recipient> <amount> <private_key>")
    else:
        recipient = sys.argv[1]
        amount = float(sys.argv[2])
        private_key = sys.argv[3]
        send_eth(recipient, amount, private_key)
