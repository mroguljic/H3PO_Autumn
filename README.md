# Installation
```
cmsrel CMSSW_12_3_0
cd CMSSW_12_3_0
cmsenv
cd ..
python3 -m venv py3env
source py3env/bin/activate
pip install --upgrade pip
pip install mplhep matplotlib root_numpy
pip install jupyter
git clone git@github.com:mroguljic/H3PO_Autumn.git
```

# Running the notebooks from a server
On server
```
cd H3PO
jupyter notebook --no-browser --port=8889 #Output shows the token which may be necessary to provide in browser on first connection
```
On local
```
ssh -N -f -L localhost:8888:localhost:8889 USER@SERVER
http://localhost:8888 #type this in a browser
```

