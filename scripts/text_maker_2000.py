from os import listdir
from os.path import isfile, join

mypath = "/STORE/matej/H3_skims/2017/QCD2000/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


	

with open("args_QCD2000.txt", "w") as args:
	for i in onlyfiles:
		print("copied file ", i)
		inpu = "-input /STORE/matej/H3_skims/2017/QCD2000/" + i
		outpu = " -output /home/fhavojic/work/H3PO_Autumn/results/QCD2000/" + i + "\n"

		put = inpu + outpu
		args.write(put)


