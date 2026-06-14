from math import ceil
from main import BloomFilter, Hasher
import pandas as pd
import time

cities = pd.read_csv("data/worldcities.csv")


cities_string = list(cities.admin_name1)

size = list(range(1000, 10001, 100))

hash_num = list(range(1, 21))

df_list = []

for m in size:    
    for k in hash_num:
        bf = BloomFilter(m, k)
        results = 0
        insert_time = []
        search_time = []
        for city_index in range(len(cities_string)):
            if city_index < 24996:
                insert_start = time.perf_counter()
                bf.insert(cities_string[city_index])
                insert_end = time.perf_counter()
                insert_time.append(insert_end - insert_start)
                continue
            search_start = time.perf_counter()
            results += bf.search(cities_string[city_index])
            search_stop = time.perf_counter()
            search_time.append(search_stop - search_start)

        temp_df = pd.DataFrame({"m" : [m], "k" : [k], "fpr": [results/int(len(cities_string[24996:]))], 
        "search": [sum(search_time)/len(search_time)], "insert": [sum(insert_time)/len(insert_time)] })
        df_list.append(temp_df)

results_df = pd.concat(df_list, ignore_index=True)

results_df.to_csv("output/data/cities_results.csv")