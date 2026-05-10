import hashlib

def bloom_hash(value, m, k):

    """ This function takes as input a value, the number m of arrays, 
    and the k number of functions, to return a list of indeces of the bloom array"""
    if isinstance(value, str):
        value = value.encode("utf-8")
    hashnum = hashlib.md5(value).hexdigest()
    h1 = int(hashnum[:16], 16)
    h2 = int(hashnum[16:], 16)
    indices = []
    for i in range(k):
        index = (h1 + i*h2)%m
        indices.append(index)
    return indices


        


