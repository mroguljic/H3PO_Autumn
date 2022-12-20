import ROOT as r

def createChainedTrees(files):
	runTree = r.TChain("Runs","Runs")
	evtTree = r.TChain("Events","Events")

	for file in files:
		runTree.Add(file)
		evtTree.Add(file)

	return runTree, evtTree

fNames = ["AA6BA5E7-75AE-E146-9E61-E529C55B4619.root",
"05210E91-3056-6944-9F5D-EA615D779312.root"
]

skimDir = "/STORE/matej/H3_skims/2017/QCD1000/"
files = [skimDir+fName for fName in fNames]

runs, events = createChainedTrees(files)

nGenEvents    = 0
for i in range(runs.GetEntries()):
	runs.GetEntry(i)
	nGenEvents+=runs.genEventCount
print("Total generated events: {0}".format(nGenEvents))

nSkimmedEvents = events.GetEntries()
print("Skimmed events: {0}".format(nSkimmedEvents))
for i in range(nSkimmedEvents):
	events.GetEvent(i)
	if(i%10000==0):
		print(i)