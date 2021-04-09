import sys
import pickle
import block
from collections import defaultdict

class Blockchain(object):
    
    def __init__(self):
        self.blocks = list()

    def Mine_Block(self, transaction):
        if len(self.blocks) == 0:
            genesis = block.Block().pow_of_block() #Genesis block
            self.blocks.append(genesis)
            print('Genesis block\n{!s}\n\n'.format(genesis))
        newblock = block.Block(len(self.blocks), transaction, self.blocks[-1].hash()).pow_of_block()
        self.blocks.append(newblock)
        print('{!s}\n\n'.format(newblock))
            
if __name__ == '__main__':
    blockchain = Blockchain()
    counter = 1
    while True:
        flag = input('keep mining?? Y or N')
        if flag.lower() == 'y':
            blockchain.Mine_Block('Block %i'%counter)
        else:    
            break
    


