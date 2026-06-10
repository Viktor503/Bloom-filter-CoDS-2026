# Bloom-filter-CoDS-2026

Benedict Pierret TAA NGUIMBIS ESSEME

Viktor Szabó

## Setting up the HPC 

```bash
cd $VSC_DATA
module load Miniforge3/25.3.0-3
source $(conda info --base)/etc/profile.d/conda.sh
conda config --append envs_dirs $VSC_DATA/conda_envs
conda config --append pkgs_dirs $VSC_SCRATCH/conda_pkgs
```

## Cloning the repository

```bash
git clone git@github.com:Viktor503/Bloom-filter-CoDS-2026.git

cd Bloom-filter-CoDS-2026
```



## Running the slurm job

```bash
sbatch benchmark.slurm
```


## Time and space complexity 


Let n be the size of the bloom filter array
Let m be the number of hash functions used

The time complexity of the get_positions function is O(m) since we need to compute m hash values for the input element.
The time complexity of insertion is also O(m) since we call get_positions and then set m bits in the bloom filter array. Giving us O(m)+O(m) = O(m)
The time complexity of the search function is also O(m) we first call get_positions to get the relevant bit positions and loopthrough them giving us O(m) + O(m) = O(m)

The space complexity of the bloom filter is O(n) because we need to store n bits.
