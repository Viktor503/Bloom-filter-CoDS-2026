from math import ceil
from main import BloomFilter, Hasher
import pandas as pd
import time 

df_strings = pd.read_csv("data/random_strings.csv")


strings_list = list(df_strings.strings)

size = list(range(1000, 10001, 100))

hash_num = list(range(1, 21))

df_list = []


for m in size:    
    for k in hash_num:
        bf = BloomFilter(m, k)
        results = 0
        insert_time = []
        search_time = []
        for string_index in range(len(strings_list)):
            if string_index < 10000:
                insert_start = time.perf_counter()
                bf.insert(strings_list[string_index])
                insert_end = time.perf_counter()
                insert_time.append(insert_end - insert_start)
                continue
            search_start = time.perf_counter()
            results += bf.search(strings_list[string_index])
            search_stop = time.perf_counter()
            search_time.append(search_stop - search_start)

        temp_df = pd.DataFrame({"m" : [m], "k" : [k], "fpr": [results/int(len(strings_list[10000:]))], 
        "search": [sum(search_time)/len(search_time)], "insert": [sum(insert_time)/len(insert_time)] })
        df_list.append(temp_df)

results_df = pd.concat(df_list, ignore_index=True)

results_df.to_csv("output/data/strings_results.csv")