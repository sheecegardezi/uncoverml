# wget -O jupyter_install.sh https://raw.githubusercontent.com/GeoscienceAustralia/uncover-ml/sheece-jupyter/jupyter/jupyter_install.sh
# chmod +x jupyter_install.sh
# ./jupyter_install.sh
# source $HOME/venvs/jupyter/bin/activate
# jupyter notebook --generate-config -y
# jupyter notebook password
# cd  $HOME
# qsub $HOME/uncoverml/jupyter/jupyter.host.sh
# nqstat_anu
# more client_cmd



module purge
module load pbs
module load python3/3.7.4
module load gdal/3.0.2

chmod +x $HOME/uncoverml/jupyter/jupyter.host.sh
chmod +x $HOME/uncoverml/jupyter/jupyter.host2.sh
chmod +x $HOME/uncoverml/jupyter/jupyter.host3.sh

python3 -m venv $HOME/uncoverml/venv
source $HOME/uncoverml/venv/bin/activate
$HOME/uncoverml/venv/bin/python -m pip install -r $HOME/uncoverml/requirements.txt
qsub $HOME/uncoverml/jupyter/jupyter.host.sh

qsub $HOME/uncoverml/jupyter/jupyter.host2.sh
qsub $HOME/uncoverml/jupyter/jupyter.host3.sh
nqstat_anu


cd $HOME && qsub $HOME/github/uncover-ml/jupyter/jupyter_pbsjob.sh
