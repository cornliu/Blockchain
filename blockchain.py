import sys
import pickle
import block
from collections import defaultdict

class Blockchain(object):
    
    def __init__(self):
        self.blocks = list()

    def Mine_Block(transaction):
        if self.blocks.length == 0:
            self.blocks.append(block.Block()).pow_of_block() #Genesis block
        newblock = block.Block(self.blocks.length, transaction, self.blocks[-1]._hash).pow_of_block()
        self.blocks.append(newblock)
            
if __name__ == '__main__':
    a = Block('aaa', '12987')
    print(a)
    


