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
