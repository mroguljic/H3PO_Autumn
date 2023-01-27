from os import listdir
from os.path import isfile, join

mypath = "/STORE/matej/H3_skims/2017/QCD1000/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


	

with open("args_QCD1000.txt", "w") as args:
	for i in onlyfiles:
		print("copied file ", i)
		inpu = "-input /STORE/matej/H3_skims/2017/QCD1000/" + i
		outpu = " -output /home/fhavojic/work/H3PO_Autumn/results/QCD1000/" + i + "\n"

		put = inpu + outpu
		args.write(put)


