import sys
import pickle

import block
import db

from collections import defaultdict

class Blockchain(object):
    
    def __init__(self):
        self.blocks = [block.Block().pow_of_block()] #Genesis block
        # print('Genesis block\n{!s}\n\n'.format(self.blocks[0]))
    def Print_BlockChain(self):
        for i in range(len(self.blocks)):
            print(self.blocks[i])
    def Mine_Block(self, transaction):
        newblock = block.Block(len(self.blocks), transaction, self.blocks[-1].hash()).pow_of_block()
        self.blocks.append(newblock)
        # print('{!s}\n\n'.format(newblock))
            



    


