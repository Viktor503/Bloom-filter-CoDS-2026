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


## Setup conda environment

```bash
conda env create -f environment.yml -n bloom_filter
conda activate bloom_filter
```
