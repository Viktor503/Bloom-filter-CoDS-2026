import pytest
from math import ceil
from main import BloomFilter, Hasher


# ---- test the hasher ----

@pytest.mark.parametrize("hashes_num, size",[
    (1,10),
    (2,100),
    (7,4000)],)
def test_hasher_init(hashes_num, size):
    hasher = Hasher(hashes_num=hashes_num,size=size)
    assert hasher.hashes_num == hashes_num
    assert hasher.size == size

# test for correct number of positions
@pytest.mark.parametrize("hashes_num, size, value",[
    (1,10,"test"),
    (2,100,"test2"),
    (7,4000,"test3")])
def test_returned_num(hashes_num, size, value):
    hasher = Hasher(hashes_num=hashes_num,size=size)
    assert len(hasher.get_positions(value=value)) == hashes_num

# test if same input for string
@pytest.mark.parametrize("hashes_num, size, value",[
    (1,10,"test"),
    (2,100,"test2"),
    (7,4000,"test3")])
def test_returned_input_same(hashes_num, size, value):
    hasher = Hasher(hashes_num=hashes_num,size=size)
    hash1 = hasher.get_positions(value=value)
    hash2 = hasher.get_positions(value=value)
    assert hash1 == hash2

# test if different input strings produce different output
@pytest.mark.parametrize("hashes_num, size, value1, value2",[
    (1,10,"dog","cat"),
    (2,100,"cat","bird"),
    (7,4000,"cat","bird")])
def test_returned_input_different(hashes_num, size, value1, value2):
    hasher = Hasher(hashes_num=hashes_num,size=size)
    hash1 = hasher.get_positions(value=value1)
    hash2 = hasher.get_positions(value=value2)
    assert hash1 != hash2

# ---- test the bloom filter ----

# test init
@pytest.mark.parametrize("hashes_num, size",[
    (1,10),
    (2,100),
    (7,4000)],)
def test_bloomfilter_init(hashes_num,size):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    assert bf.size == size
    assert bf.hashes_num == hashes_num
    assert bf._insert_count == 0

# test bytearray size
@pytest.mark.parametrize("hashes_num, size, bytearray_size",[
    (1, 10, 16),
    (2, 100, 104),
    (7, 4000, 4000)],)
def test_bloomfilter_bytearray_len(hashes_num, size, bytearray_size):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    # we have to multipy by 8 to get bits and not bytes
    assert len(bf.data)*8 == bytearray_size

# test hasher initialization
@pytest.mark.parametrize("hashes_num, size, bytearray_size",[
    (1, 10, 16),
    (2, 100, 104),
    (7, 4000, 4000)],)
def test_bloomfilter_hasher_init(hashes_num, size, bytearray_size):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    assert bf.hasher.hashes_num == hashes_num
    assert bf.hasher.size == size


# test if self.data different after insert than different from before insert
@pytest.mark.parametrize("hashes_num, size, value",[
    (1,10,"test"),
    (2,100,"test2"),
    (7,4000,"test3")])
def test_data_changed(hashes_num, size, value):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    prev_data = bytearray(bf.data)
    bf.insert(value)
    assert prev_data != bf.data

# test if second insertion of same value changes self.data
@pytest.mark.parametrize("hashes_num, size, value",[
    (1,10,"test"),
    (2,100,"test2"),
    (7,4000,"test3")])
def test_data_unchanged(hashes_num, size, value):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    bf.insert(value)
    prev_data = bytearray(bf.data)
    bf.insert(value)
    assert prev_data == bf.data

# inserted word is found by search
@pytest.mark.parametrize("hashes_num, size, value",[
    (1,10,"test"),
    (2,100,"test2"),
    (7,4000,"test3")])
def test_insertion_search(hashes_num, size, value):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    bf.insert(value)
    assert bf.search(value) is True

# seach for uninserted word
@pytest.mark.parametrize("hashes_num, size, value1, value2",[
    (1,10,"dog","cat"),
    (2,100,"cat","bird"),
    (7,4000,"cat","bird")])
def test_uninserted_search(hashes_num, size, value1, value2):
    bf = BloomFilter(size=size,hashes_num=hashes_num)
    bf.insert(value1)
    assert bf.search(value2) is False

# test if data_binary returns correct string
@pytest.mark.parametrize("hashes_num, size, expected", [
    (1, 10, "00000000_00000000"),
    (2, 20, "00000000_00000000_00000000"),
    (1, 6, "00000000")
    ])
def test_all_zeros_on_empty_filter(hashes_num, size, expected):
    assert BloomFilter(size=size, hashes_num=hashes_num).data_binary() == expected