from main import BloomFilter
from pathlib import Path
from typing import List
import random
import time
import pandas as pd
from matplotlib import pyplot as plt


class Benchmark:
    def __init__(
        self,
        data: List[str],
        sizes: List[int],
        hash_funcs: List[int],
        insert_nums: List[int],
        test_nums: List[int],
    ) -> None:
        self.data = data
        self.sizes = sizes
        self.hash_funcs = hash_funcs
        self.insert_nums = insert_nums
        self.test_nums = test_nums

    def run_experiment(
        self,
        output_path: str | Path = "results.csv",
        seed: int = 42,
    ):
        random.seed(seed)

        results = []

        # loop through all sizes and hash_function numbers
        for n in self.sizes:
            for m in self.hash_funcs:
                # loop through insertion and test numbers
                for insert_num in self.insert_nums:
                    for test_num in self.test_nums:
                        # Create bloom filter
                        bf = BloomFilter(size=n, hashes_num=m)
                        # create train and test data
                        deduplicated_data = list(set(self.data))
                        train_data = random.sample(deduplicated_data, insert_num)
                        remaining = list(set(deduplicated_data) - set(train_data))
                        test_data = random.sample(remaining, test_num)

                        # insert train_data and start timing
                        insert_started = time.time()
                        for item in train_data:
                            bf.insert(item)
                        #  stop timing insertion
                        insertion_elapsed = round(
                            (time.time() - insert_started) * 1000, 6
                        )

                        false_positives = 0
                        search_started = time.time()
                        for item in test_data:
                            false_positives += bf.search(item)
                        search_elapsed = round((time.time() - search_started) * 1000, 6)

                        fpr = round(false_positives / test_num, 2)
                        analytical_fpr = round(bf.false_positive_rate(), 2)

                        results.append(
                            {
                                "n": n,
                                "m": m,
                                "inserted": insert_num,
                                "tested": test_num,
                                "fpr": fpr,
                                "fpr (analytical)": analytical_fpr,
                                "insert_time (ms)": insertion_elapsed,
                                "search_time (ms)": search_elapsed,
                            }
                        )

        df = pd.DataFrame(results)
        df.to_csv(
            output_path,
        )


def plot_time(
    result_path: str | Path = "results.csv",
):
    # read csv
    df = pd.read_csv(result_path)

    # insert time vs insertnum + hash_func
    size = df.iloc[0]["n"]
    hash_func_nums = df["m"].unique()

    for hash_func_num in hash_func_nums:
        part = df[(df["m"] == hash_func_num) & (df["n"] == size)]
        plt.plot(
            part["inserted"],
            part["insert_time (ms)"],
            marker="o",
            label=f"m = {hash_func_num}",
        )
    plt.title(f"Insertion results for size={size}")
    plt.xlabel("inserted items")
    plt.ylabel("insert time")
    plt.legend()
    plt.savefig("insert_time.png")
    plt.show()

    # search_time vs insertnum + hash_func
    for hash_func_num in hash_func_nums:
        part = df[(df["m"] == hash_func_num) & (df["n"] == size)]
        plt.plot(
            part["inserted"],
            part["search_time (ms)"],
            marker="o",
            label=f"m = {hash_func_num}",
        )
    plt.title(f"Search results for size={size}")
    plt.xlabel("inserted items")
    plt.ylabel("search time")
    plt.legend()
    plt.savefig("search_time.png")
    plt.show()


def plot_fpr(
    result_path: str | Path = "results.csv",
):
    # read csv
    df = pd.read_csv(result_path)

    # fpr vs insertnum
    size = df.iloc[0]["n"]
    hash_func_nums = df["m"].unique()

    for hash_func_num in hash_func_nums:
        part = df[(df["m"] == hash_func_num) & (df["n"] == size)]
        plt.plot(
            part["inserted"],
            part["fpr"],
            marker="o",
            label=f"m = {hash_func_num} actual",
        )
        plt.plot(
            part["inserted"],
            part["fpr (analytical)"],
            marker="o",
            linestyle="dashed",
            label=f"m = {hash_func_num} analytical",
        )
    plt.title(f"False positive rate predictiosn for size={size}")
    plt.xlabel("inserted items")
    plt.ylabel("fpr")
    plt.legend()
    plt.savefig("fpr_plot.png")
    plt.show()


if __name__ == "__main__":

    # Test with natutal language words 
    cities = pd.read_csv("data/worldcities.csv")

    cities_string = list(cities.admin_name1)

    print(len(cities_string))  # total rows
    print(len(set(cities_string)))  # unique values
    b = Benchmark(
        data=cities_string,
        sizes=[1000, 5000, 10000],
        hash_funcs=[1, 2, 3],
        insert_nums=list(range(100, 2000, 100)),
        test_nums=[1000],
    )
    b.run_experiment()

    plot_time()
    plot_fpr()

    # Test with random string of data

     # Test with natutal language words 
    df_strings = pd.read_csv("data/random_strings.csv")

    strings_list = list(df_strings.strings)
    
    print(len(strings_list))  # total rows
    print(len(set(strings_list)))  # unique values
    r = Benchmark(
        data=strings_list,
        sizes=[1000, 5000, 10000],
        hash_funcs=[1, 2, 3],
        insert_nums=list(range(100, 2000, 100)),
        test_nums=[1000],
    )
    r.run_experiment()

    plot_time()
    plot_fpr()