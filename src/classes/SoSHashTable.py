class SoSHashTable:
    def __init__(self, capacity=10):
        self.__table = []
        for i in range(capacity):
            self.__table.append([])
        self.__size = capacity

    def __determine_bucket(self, seed):
        return hash(seed) % self.__size

    def insert(self, item, key):
        bucket_index = self.__determine_bucket(key)
        if not self.get(key):
            self.__table[bucket_index].append([key, item])

    def get(self, key):
        bucket_index = self.__determine_bucket(key)
        bucket = self.__table[bucket_index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        bucket_index = self.__determine_bucket(key)
        bucket = self.__table[bucket_index]
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                break
