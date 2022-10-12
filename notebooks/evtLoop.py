import ROOT as r

testFileName = "/STORE/ferencek/TRSM_XToHY_6b/2017/13TeV/NANOAOD/TRSM_XToHY_6b_M3_2000_M2_1100_NANOAOD.root"

f 		= r.TFile.Open(testFileName)
tree 	= f.Get("Events")

for i in range(100):
	tree.GetEvent(i)
	print(tree.nFatJet)