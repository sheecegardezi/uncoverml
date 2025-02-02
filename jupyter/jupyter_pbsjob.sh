
#!/bin/bash
#PBS -N uncoverml
#PBS -P ge3
#PBS -q gpuvolta
#PBS -l walltime=24:00:00
#PBS -l ncpus=24
#PBS -l ngpus=2
#PBS -l mem=192GB
#PBS -l jobfs=100GB
#PBS -l storage=gdata/ge3
module purge
module load pbs
module load python3/3.7.4
module load gdal/3.0.2

set -e
ulimit -s unlimited


# activate the virtual env you have created
source $PBS_O_WORKDIR/venvs/uncoverml_gadi/bin/activate



export jport=8388  # choose a port number

echo "Starting Jupyter lab ..."
jupyter lab --no-browser --ip=`hostname` --port=${jport} &

echo "client_cmd created ..."
cd $PBS_O_WORKDIR


echo "ssh -N -L ${jport}:`hostname`:${jport} ${USER}@gadi.nci.org.au &" > client_cmd

sleep infinity
