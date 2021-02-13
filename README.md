# uncoverml

https://python-data-science.readthedocs.io/en/latest/general.html


ssh sg4953@gadi.nci.org.au
nqstat_anu

pangeo.ini.all.sh

ls /g/data/ge3/sheece/*.ipynb 

'/g/data/ge3/sheece/Bayesian Search.ipynb'
'/g/data/ge3/sheece/Feature Ranking.ipynb'
'/g/data/ge3/sheece/Grid Search.ipynb'
'/g/data/ge3/sheece/Pre Processing.ipynb'
'/g/data/ge3/sheece/Testing F-Rank.ipynb'
'/g/data/ge3/sheece/xgboost.ipynb'

scp sg4953@gadi.nci.org.au:/g/data/ge3/sheece/*.ipynb /home/dev/Desktop/new_uncoverml/backup

python3 -m venv /home/dev/Desktop/new_uncoverml/venv
source venv/bin/activate
deactivate

pip install -U arrow
pip list
pip install -r requirements.txt

jupyter-lab

scp sg4953@gadi.nci.org.au:/home/547/sg4953/github/uncover-ml/notebooks/Workflow.ipynb /home/dev/Desktop/Work/uncoverml

"# /apps/pangeo/2020.05/bin/python -m pip install --user rasterio\n",
"# /apps/pangeo/2020.05/bin/python -m pip install --user wheel\n",
"# /apps/pangeo/2020.05/bin/python -m pip install --user fiona\n",
"# /apps/pangeo/2020.05/bin/python -m pip install --user xgboost\n",
"# /apps/pangeo/2020.05/bin/python -m pip install --user lightgbm\n",
"# /apps/pangeo/2020.05/bin/python -m pip install --user graphviz"



#xgboost
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
git submodule init
git submodule update
mkdir build
cd build
cmake .. -DCMAKE_C_COMPILER=/usr/bin/gcc-8 -DCMAKE_CXX_COMPILER=/usr/bin/g++-8 -DUSE_CUDA=ON -DUSE_NCCL=ON  -DNCCL_ROOT=/usr/local/nccl-2.8.3/
make -j1

cd ../python-package
pwd
python setup.py install --use-cuda --use-nccl


#catboost
git clone https://github.com/catboost/catboost.git
sudo apt-get install libc6-dev






LD_LIBRARY_PATH="/usr/local/nccl-2.8.3:/usr/lib/cuda"
sudo ln -s /usr/local/nccl-2.8.3/include/nccl.h /usr/include/nccl.h


scp sg4953@gadi.nci.org.au:/home/547/sg4953/notebooks/*.ipynb /home/dev/Desktop/new_uncoverml/backup

ssh sg4953@gadi.nci.org.au

ssh dev@103.22.145.172