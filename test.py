import ROOT as r

f 		= r.TFile.Open("test.root")
events 	= f.Get("Events")

for i,event in enumerate(events): 
    if i % 1000 :
    	print(i)

    tH1 = ROOT.TLorentzVector()
    tH1.SetPtEtaPhiE(h[0].pt(),h[0].eta(),h[0].phi(),h[0].energy())

    tH2 = ROOT.TLorentzVector()
    tH2.SetPtEtaPhiE(h[1].pt(),h[1].eta(),h[1].phi(),h[1].energy())

    tH3 = ROOT.TLorentzVector()
    tH3.SetPtEtaPhiE(h[2].pt(),h[2].eta(),h[2].phi(),h[2].energy())

    lv_123 = tH1+tH2+tH3
    lv_12  = tH1+tH2
    ...


