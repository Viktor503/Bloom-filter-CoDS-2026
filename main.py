


class hasher(object):
    """
    Class Responsible for hashing input data
    """

    def __init__(self, numBuckets:int): # To initiate the hashtable with a number of predefined buckets
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(self.numBuckets):
            self.buckets.append([])
    
    def addEntry(self, key, value):
        """Adding entries to the hash table. Appends a tuple of key and value to the hash postion"""
        keyhash = hash(key)
        hashbucket = self.buckets[keyhash%self.numBuckets]
        for i in range(len(hashbucket)):
            if hashbucket[i][0] == keyhash:
                hashbucket[i] = (keyhash, value)
                return
        hashbucket.append((keyhash, value))
        
    def get_value(self, key) :
        """
        Returns the value associated with the key provided        
        """
        keyhash = hash(key)
        hashbucket = self.buckets[keyhash%self.numBuckets]
        for e in hashbucket:
            if hashbucket[0] == keyhash:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' 



class BloomFilter:
    """
    Bloom filter class
    """

    def __init__(self, size, hashes_num):
        self.size = size
        self.hashes_num = hashes_num
        self.data = [0]*size
        self._insert_count = 0
        self.hasher = Hasher(hashes_num=hashes_num, size=size)

    def insert(self, element: str):
        """
        Hash element and store results in self.data

        Args:
            element (str): element we want to store
        """
        raise NotImplementedError()

    def search(self, element: str) -> bool:
        """

        Args:
            element (str): element we want to look up

        Returns:
            bool: returns if item is probably included in the bloom filter
        """
        raise NotImplementedError()

    def __repr__(self) -> str:
        """
        Print basic statistics from the bloom filter

        Returns:
            str: bloom filter summary string
        """
        raise NotImplementedError()
