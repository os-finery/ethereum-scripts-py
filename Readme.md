# Ethereum Transaction Script with Web3.py

**Important:** Keep your private key safe! Do not share it with anyone.\
**Important:** After copy-paste clear you buffer(simply copy something else).

## Prerequisites

- Python 3.7+
- Pip

## Installation

1. Install Python packages:

```sh
pip install web3 eth-account
```
or
```sh
pip3 install web3 eth-account
```

## Usage

### 1. Generate Public and Private Keys

To generate a new Ethereum account:

```sh
python generate-public-private-key.py
```
or 
```sh
python3 generate-public-private-key.py
```

This script will output your private key and public address.

### 2. Send Ethereum to an Address

Use the `send-eth-to-address.py` script to send Ethereum to a specified address.

```sh
python send-eth-to-address.py <recipient> <amount> <private_key>
```
or 
```sh
python3 send-eth-to-address.py <recipient> <amount> <private_key>
```

- `<recipient>`: Ethereum address of the recipient(example: 0xDB5AcAb0510759e3a01a4832984EE476Fc35E905)
- `<amount>`: Amount of Ether to send in ETH (example: 0.01)
- `<private_key>`: Private key of the sender(example: 0x84c755b33c835f13775c49a52cb4138298151e83726f1d72f57895ebfaafb661)

Example:

```sh
python send-eth-to-address.py 0xRecipientAddressHere 0.01 0xYourPrivateKeyHere
```