import ROOT as r
import json

def zbrajanje():
	filename_list = ["QCD1000","QCD1500", "QCD2000", "QCD700"]

	f = r.TFile.Open("QCD1000_total.root")

	hist_1000 = f.trijetm_1000

	hist_ult = hist_1000.Clone("trijetm_ult")
	#print(type(hist_ult), type(hist_1000))
	hist_ult.Reset()

	broj = hist_ult.Integral()
	print(broj)


	with open("norma.json", "r") as nora:
		dict_norma = json.load(nora)

	for name in filename_list:
		filename = name + "_total.root"

		g = r.TFile.Open(filename) #ime novog file-a mora biti drugačije od onog gore, inače program izgubi informaciju o kloniranom histogramu

		if "1000" in filename:
			hist_stari = g.trijetm_1000 #mozda ovo treba odvojiti ako već imam otvoren QCD1000 file
		elif "1500" in filename:
			hist_stari = g.trijetm_1500
		elif "2000" in filename:
			hist_stari = g.trijetm_2000
		else:
			hist_stari = g.trijetm_700


		norma = dict_norma[name]
		print(norma)
		#print(type(hist_ult))
		hist_ult.Add(hist_stari, norma)
		#treba još i spremiti

		broj2 = hist_ult.Integral()
		print(broj2)





zbrajanje()