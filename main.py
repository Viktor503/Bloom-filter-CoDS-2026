class Hasher:
    """
    Class Responsible for hashing input data
    """

    def __init__(self, hashes_num, size):
        self.hashes_num = hashes_num
        self.size = size

    def get_positions(self, item: str) -> list[int]:
        """
        Implements item hashing with self.hashes_num hash functions

        Args:
            item (str): the item we are hashing

        Returns:
            list[int]: output results of the hash
        """
        raise NotImplementedError()


class BloomFilter:
    """
    Bloom filter class
    """

    def __init__(self, size, hashes_num):
        self.size = size
        self.hashes_num = hashes_num
        self.data = bytearray(ceil(size / 8))
        self._insert_count = 0
        self.hasher = Hasher(hashes_num=hashes_num, size=size)

    def insert(self, element: str):
        """
        Hash element and store results in self.data

        Args:
            element (str): element we want to store
        """
        positions = self.hasher.get_positions(element)
        for position in positions:
            element_bit = 1 << (position % 8 )
            self.data[-position//8] |= element_bit
        self._insert_count += 1

    def search(self, element: str) -> bool:
        """

        Args:
            element (str): element we want to look up

        Returns:
            bool: returns if item is probably included in the bloom filter
        """
        positions = self.hasher.get_positions(element)
        for position in positions:
            element_bit = 1 << (position % 8 )
            if not self.data[-position//8] & element_bit:
                return False
        return True

    def __repr__(self) -> str:
        """
        Print basic statistics from the bloom filter

        Returns:
            str: bloom filter summary string
        """
        return (
            f"*****\n"
            f"BloomFilter:\n"
            f"size: {self.size}\n"
            f"num_hashes: {self.hashes_num}\n"
            f"inserted items: {self._insert_count}\n"
            f"*****"
        )
    
    def data_binary(self) -> str:
        """Returns the data in a binary string matrix

        Returns:
            str: The returned bytearray as bits
        """
        return '_'.join([format(x,"08b") for x in self.data])



if __name__ == "__main__":
    bf = BloomFilter(10,2)
    print(bf)
    bf.insert("test")
    print(bf.data_binary())
    bf.insert("test2")
    bf.insert("test3")
    print(bf.data_binary())
    print(bf.search("test"))
    print(bf.search("test2"))
    print(bf.search("test3"))
    print(bf.search("test4"))
