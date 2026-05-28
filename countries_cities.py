from math import ceil
from main import BloomFilter, Hasher
import pandas as pd

cities = pd.read_csv("data/worldcities.csv")


cities_string = list(names.admin_name)

size = list(range(1000, len(cities.index), 100))

hash_num = list(range(1, 21))

params = []

for m in size:    
    for k in hash_num:
        bf = BloomFilter(m, k)
        results = 0
        for city_index in range(cities_string):
            if city_index < m:
                bf.insert(cities_string[city_index])
                continue
            results += bf.search(cities_string[city_index])
        params.append((m, k, results/int(len(cities_string[m:]))))