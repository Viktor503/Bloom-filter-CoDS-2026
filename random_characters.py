from math import ceil
from main import BloomFilter, Hasher
import pandas as pd

df_strings = pd.read_csv("data/random_strings.csv")


strings_list = list(df_strings.strings)

size = list(range(1000, len(df_strings.index), 100))

hash_num = list(range(1, 21))

df_list = []

for m in size:    
    for k in hash_num:
        bf = BloomFilter(m, k)
        results = 0
        for string_index in range(len(strings_list)):
            if string_index < m:
                bf.insert(strings_list[string_index])
                continue
            results += bf.search(strings_list[string_index])
            temp_df = pd.DataFrame({"m" : [m], "k" : [k], "fpr": [results/int(len(strings_list[m:]))]})
        df_list.append(temp_df)

results_df = pd.concat(df_list, ignore_index=True)

results_df.to_csv("output/data/strings_results.csv")