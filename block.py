import time
import utils
from pow import Pow

class Block(object):
    def __init__(self, block_height=0, transaction='GenesisBlock', prev_block_hash=''):
        self._height = block_height
        self._prev_block_hash = utils.encode(prev_block_hash)
        self._timestamp = utils.encode(str(int(time.time())))
        self._nonce = 0
        self._bits = 8
        self._transaction = transaction
        self._hash = None
    
    def __repr__(self):
        return 'Block(timestamp={0!r}, transaction={1!r}, prev_block_hash={2!r}, hash={3!r}, nonce={4!r}, height={5!r})'.format(
            self._timestamp, self._transaction, self._prev_block_hash, self._hash, self._nonce, self._height)

    def pow_of_block(self):
        pow = Pow(self)
        nonce, hash = pow.run()
        self._nonce, self._hash = nonce, utils.encode(hash)
        return self


    def hash(self):
        return utils.decode(self._hash)

    def prev_block_hash(self):
        return utils.decode(self._prev_block_hash)

    def timestamp(self):
        return str(self._timestamp)

    def nonce(self):
        return str(self._nonce)

    def transactions(self):
        return self._transaction
    


