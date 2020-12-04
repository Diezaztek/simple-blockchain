import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = list()
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof: int, previous_hash: str) -> None:
        block = {
                'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash
            }
        
        self.chain.append(block)
        return block