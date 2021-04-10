import pickle
from collections import defaultdict

import blockchain

class DB(object):

    def __init__(self, db_file):
        self._db_file = db_file
        try:
            with open(self._db_file, 'rb') as f:
                self.kv = pickle.load(f)  
        except:
            with open(self._db_file, 'wb') as f:
                newblockchain = blockchain.Blockchain()
                pickle.dump(newblockchain, f)
                self.kv = newblockchain
    def save(self, blockchain):
        with open(self._db_file, 'wb') as f:
            pickle.dump(blockchain, f)
    def reset(self):
        with open(self._db_file, 'wb') as f:
            pickle.dump('', f)
    def load(self):
        with open(self._db_file, 'rb') as f:
            return pickle.load(f)
    
