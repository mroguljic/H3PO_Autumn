from os import listdir
from os.path import isfile, join

mypath = "/STORE/matej/H3_skims/2017/QCD700/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


	

with open("args_QCD700.txt", "w") as args:
	for i in onlyfiles:
		print("copied file ", i)
		inpu = "-input /STORE/matej/H3_skims/2017/QCD700/" + i
		outpu = " -output /home/fhavojic/work/H3PO_Autumn/results/" + i + "\n"

		put = inpu + outpu
		args.write(put)


