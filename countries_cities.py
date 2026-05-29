from math import ceil
from main import BloomFilter, Hasher
import pandas as pd

cities = pd.read_csv("data/worldcities.csv")


cities_string = list(cities.admin_name1)

size = list(range(1000, len(cities.index), 100))

hash_num = list(range(1, 21))

df_list = []

for m in size:    
    for k in hash_num:
        bf = BloomFilter(m, k)
        results = 0
        for city_index in range(len(cities_string)):
            if city_index < m:
                bf.insert(cities_string[city_index])
                continue
            results += bf.search(cities_string[city_index])
            temp_df = pd.DataFrame({"m" : m, "k" : k, "fpr": results/int(len(cities_string[m:]))})
        df_list.append(temp_df)

results_df = pd.concat(df_list, ignore_index=True)

results_df.to_csv("output/data/cities_results.csv")