# Nonce Mining Simulation

# 1. Add Mining Function:

import time
import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        attempts = 0
        start_time = time.time()
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1
        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")


# 2. Mine a Block:

difficulty = 4  # Hash must start with '0000'
block = Block(1, "Test Mining Block", "some_previous_hash")
block.mine_block(difficulty)