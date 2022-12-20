#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /users/mrogul/Work/Autumn_project/CMSSW_12_3_0/
eval `scramv1 runtime -sh`
cd /users/mrogul/Work/Autumn_project
source py3env/bin/activate

export WORK_DIR=/users/mrogul/Work/Autumn_project/H3PO_Autumn/scripts/
cd $WORK_DIR

python $WORK_DIR/Processor.py $*
 
