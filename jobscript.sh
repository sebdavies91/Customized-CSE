#!/bin/bash -l
# Use the current working directory and current environment for this job.
#SBATCH -D ./
#SBATCH --export=ALL
# Define an output file - will contain error messages too
#SBATCH -o hello%j.out
# Define job name
#SBATCH -J SD_CSE
# Request 1 core 1 node
#SBATCH -N1 -n9
# This asks for 10 minutes of time.
#SBATCH --mem-per-cpu=8000M
# Insert your own username to get e-mail notifications
#SBATCH --mail-user=<username>@liverpool.ac.uk
#SBATCH --mail-type=ALL
#SBATCH -p lowpriority
#SBATCH -t 24:00:00

echo =========================================================
echo SGE job: submitted  date = `date`
date_start=`date +%s`

rm 9x9outputsmakemecry2

conda deactivate
module load compilers/intel/2019u5
module load libs/intel/2019u5   
module load apps/anaconda3/2020.02  
export PYTHONPATH=/users/srdavies/Lotus/Lotus/
export LOTUS_HOME=/users/srdavies/Lotus/Lotus/
conda activate lotus-env 
echo "Run executable:"
python run.py echo > Output.txt &
wait
echo "End of execution"

