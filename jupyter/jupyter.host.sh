#!/bin/bash 
#PBS -N uncoverml 
#PBS -P ge3 
#PBS -q gpuvolta
#PBS -l walltime=12:00:00 
#PBS -l ncpus=12
#PBS -l ngpus=1
#PBS -l mem=96GB
#PBS -l jobfs=100GB 
#PBS -l storage=gdata/ge3 
module purge
module load pbs
module load python3/3.7.4
module load gdal/3.0.2

set -e
ulimit -s unlimited

if [ -e ${PBS_O_WORKDIR}/client_cmd  ]; then
    rm  ${PBS_O_WORKDIR}/client_cmd
fi

module purge
module load pbs
module load python3/3.7.4
module load gdal/3.0.2
source $PBS_O_WORKDIR/uncoverml/venv/bin/activate

export jport=8391

echo "Jupyter lab started ..."
jupyter lab --no-browser --ip=`hostname` --port=${jport} &

echo "client_cmd created ..."
cd $PBS_O_WORKDIR
echo "ssh -N -L ${jport}:`hostname`:${jport} ${USER}@gadi.nci.org.au &" > client_cmd

sleep infinity

