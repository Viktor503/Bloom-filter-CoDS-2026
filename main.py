


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

    def __init__(self, m:int, k:int):
        self.m = m
        self.k = k
        self.data = [0]*m
        self._insert_count = 0
        

    def add_entry(self, element:str):

        """ This function stores hashed elements in self.data.
            Args:
                element (str): the element we want to store
        """
        if isinstance(element, str):
            element = element.encode("utf-8")
        hashnum = hashlib.md5(element).hexdigest()
        h1 = int(hashnum[:16], 16)
        h2 = int(hashnum[16:], 16)
        for i in range(self.k):
            index = (h1 + i*h2)%self.m
            self.data[index] = 1
            self._insert_count += 1           

    def find(self, element: str) -> bool:
        """

        Args:
            element (str): element we want to look up

        Returns:
            bool: returns if item is probably included in the bloom filter
        """
        if isinstance(element, str):
            element = element.encode("utf-8")
        hashnum = hashlib.md5(element).hexdigest()
        h1 = int(hashnum[:16], 16)
        h2 = int(hashnum[16:], 16)
        indices = []
        for i in range(self.k):
            index =  (h1 + i*h2)%self.m
            indices.append(index)
        for y in indices:
            if self.data[y] == 1:
                prob = (1.0 - ((1.0 - 1.0/self.m)**(self.k*self._insert_count))) ** self.k
                return "Might be in bloom filter with a false positive probability of " + str(prob)
        return "Not found in bloom filter"

    

    def __repr__(self) -> str:
        """
        Print basic statistics from the bloom filter

        Returns:
            str: bloom filter summary string
        """
        raise NotImplementedError()
