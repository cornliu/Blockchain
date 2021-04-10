import pickle
from collections import defaultdict

class DB(object):

    def __init__(self, db_file):
        self._db_file = db_file
    def save(self, blockchain):
        with open(self._db_file, 'wb') as f:
            pickle.dump(blockchain, f)
    def reset(self):
        with open(self._db_file, 'wb') as f:
            pickle.dump('', f)
    def load(self):
        with open(self._db_file, 'rb') as f:
            return pickle.load(f)
    
