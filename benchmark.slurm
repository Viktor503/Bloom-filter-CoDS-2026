#!/bin/bash -l
#SBATCH --cluster=genius
#SBATCH --account=$VSC_ACCOUNT
#SBATCH --time=00:15:00
#SBATCH --partition=batch_skylake

module load Miniforge3/25.3.0-3
source $(conda info --base)/etc/profile.d/conda.sh
conda activate bloom_filter

python benchmark.py