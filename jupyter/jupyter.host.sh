#!/bin/bash 
#PBS -N uncoverml 
#PBS -P ge3 
#PBS -q express 
#PBS -l walltime=12:00:00 
#PBS -l ncpus=48 
#PBS -l mem=192GB 
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
source $PBS_O_WORKDIR/venvs/jupyter/bin/activate

export jport=8388

echo "Jupyter lab started ..."
jupyter lab --no-browser --ip=`hostname` --port=${jport} &

echo "client_cmd created ..."
echo "ssh -N -L ${jport}:`hostname`:${jport} ${USER}@gadi.nci.org.au &" > client_cmd

sleep infinity