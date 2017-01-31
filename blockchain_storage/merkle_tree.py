import hashlib


class MerkleTree:
    @staticmethod
    def calculate_merkle_root(data):
        return None

    def merkle(self, hashList):
        if len(hashList) == 1:
            return hashList[0]
        newHashList = []
        # Process pairs. For odd length, the last is skipped
        for i in range(0, len(hashList) - 1, 2):
            newHashList.append(self.hash2(hashList[i], hashList[i + 1]))
        if len(hashList) % 2 == 1:  # odd, hash last item twice
            newHashList.append(self.hash2(hashList[-1], hashList[-1]))
        return self.merkle(newHashList)  # TODO unroll recursion call

    def hash2(self, a, b):
        # Reverse inputs before and after hashing
        # due to big-endian / little-endian nonsense
        a1 = a.decode('hex')[::-1]
        b1 = b.decode('hex')[::-1]
        h = hashlib.sha256(hashlib.sha256(a1 + b1).digest()).digest()
        return h[::-1].encode('hex')

    def recalculate_merkle_tree(self):
        # TODO merkle tree recalculation
        pass