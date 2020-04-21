from hashlib import sha256
import json
import time

class BlockUtil:
    def __init__(self, block):
        self.index = block.id
        self.transactions = str(block.product_id) + str(block.product_status) + block.username + block.datetime
        self.previous_hash = block.previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        #block_string = self.transactions+str(self.nonce)
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def proof_of_work(self):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        self.nonce = 0

        computed_hash = self.compute_hash()
        while not computed_hash.startswith('0' * 5):
            self.nonce += 1
            computed_hash = self.compute_hash()
            print(computed_hash)
        print('最终结果是:{}, 随机数:{}'.format(computed_hash, self.nonce))

        return computed_hash