import hashlib
import sys

import utils

class Pow(object):
    
    max_nonce = sys.maxsize
    target_bits = 8

    def __init__(self, block):
        self._block = block
        self._target = 1 << (256 - self._block._bits)
    
    def _prepare_data(self, nonce):
        data_lst = [str(self._block._prev_block_hash),
                    str(self._block._transaction),
                    str(self._block._height),
                    str(self._block._timestamp),
                    str(self._block._bits),
                    str(nonce)]
        return utils.encode(''.join(data_lst))
    
    def validate(self):
        # Validates a block's PoW
        data = self._prepare_data(self._block.nonce)
        hash_hex = utils.sum256_hex(data)
        hash_int = int(hash_hex, 16)

        return True if hash_int < self._target else False
    
    def run(self):
        # Performs a proof-of-work
        nonce = 0

        while nonce < self.max_nonce:
            data = self._prepare_data(nonce)
            hash_hex = utils.sum256_hex(data)
            hash_int = int(hash_hex, 16)

            if hash_int < self._target:
                break
            else:
                nonce += 1

        return nonce, hash_hex