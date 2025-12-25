import hashlib
import json
from time import time
from typing import List, Dict, Any
from dataclasses import dataclass, asdict

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Dict[str, Any]]
    proof: int
    previous_hash: str

    def hash(self) -> str:
        """Creates a SHA-256 hash of a Block"""
        block_string = json.dumps(asdict(self), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    FinTech Private Chain
    Used for immutable audit logging of financial transactions.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        
        # Genesis Block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof: int, previous_hash: str = None) -> Block:
        """
        Create a new Block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash or self.chain[-1].hash(),
        )

        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Creates a new transaction to go into the next Mined Block
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - p is the previous proof, and p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def is_chain_valid(self, chain: List[Block]) -> bool:
        """
        Determine if a given blockchain is valid
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            
            # Check 1: Previous hash match
            if block.previous_hash != last_block.hash():
                return False

            # Check 2: Proof of Work validity
            if not self.valid_proof(last_block.proof, block.proof):
                return False

            last_block = block
            current_index += 1

        return True

# Example Usage
if __name__ == "__main__":
    blockchain = Blockchain()
    print("Mining FinTech Block 1...")
    
    # Add transactions
    blockchain.new_transaction("Bank_A", "Bank_B", 1000)
    blockchain.new_transaction("Bank_B", "Client_C", 50)
    
    # Mine
    last_proof = blockchain.last_block.proof
    proof = blockchain.proof_of_work(last_proof)
    block = blockchain.new_block(proof)
    
    print(f"[BLOCK MINED] Index: {block.index}")
    print(f"Hash: {block.hash()}")
    print(f"Transactions: {len(block.transactions)}")
    print(f"Chain Valid? {blockchain.is_chain_valid(blockchain.chain)}")
