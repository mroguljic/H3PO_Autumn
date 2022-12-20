import ROOT as r
from argparse import ArgumentParser
import json

def histogram(filename,output):    
    f = r.TFile.Open(filename)
    nGenEvents    = 0
    runs = f.Get("Runs")
    for i in range(runs.GetEntries()):
        runs.GetEntry(i)
        nGenEvents+=runs.genEventCount


    tree = f.Get("Events")
    
    if "QCD700" in filename:
        hDijet01Masses = r.TH1F("dijet01m_700","",60,0,3000)
        hDijet02Masses = r.TH1F("dijet02m_700","",60,0,3000)
        hDijet12Masses = r.TH1F("dijet12m_700","",60,0,3000)
        hTrijet012Masses = r.TH1F("trijetm_700","",60,0,3000)
        
    elif "QCD1000" in filename:
        hDijet01Masses = r.TH1F("dijet01m_1000","",60,0,3000)
        hDijet02Masses = r.TH1F("dijet02m_1000","",60,0,3000)
        hDijet12Masses = r.TH1F("dijet12m_1000","",60,0,3000)
        hTrijet012Masses = r.TH1F("trijetm_1000","",60,0,3000)
        
    elif "QCD1500" in filename:
        hDijet01Masses = r.TH1F("dijet01m_1500","",60,0,3000)
        hDijet02Masses = r.TH1F("dijet02m_1500","",60,0,3000)
        hDijet12Masses = r.TH1F("dijet12m_1500","",60,0,3000)
        hTrijet012Masses = r.TH1F("trijetm_1500","",60,0,3000)
    
    elif "QCD2000" in filename:
        hDijet01Masses = r.TH1F("dijet01m_2000","",60,0,3000)
        hDijet02Masses = r.TH1F("dijet02m_2000","",60,0,3000)
        hDijet12Masses = r.TH1F("dijet12m_2000","",60,0,3000)
        hTrijet012Masses = r.TH1F("trijetm_2000","",60,0,3000)

    nEvts = tree.GetEntriesFast()
    nPass = 0
    for i in range(nEvts): 
        tree.GetEvent(i)


        if tree.nFatJet<3:
            continue

        pts     = tree.FatJet_pt
        etas    = tree.FatJet_eta
        phis    = tree.FatJet_phi
        masses  = tree.FatJet_msoftdrop

        with open("cuts.json", "r") as cuts:
            cuts_dict = json.load(cuts)

        cuts_list = list(cuts_dict.values())

        cut_pts = cuts_list[0]
        cut_etas = cuts_list[1]
        cut_masses = cuts_list[2]

        cut_masses_min = cuts_list[2]
        cut_masses_max = cuts_list[3]
    
    

        jet0Flag = pts[0]>cut_pts and abs(etas[0])<cut_etas  and masses[0]>cut_masses_min and masses[0]<cut_masses_max
        jet1Flag = pts[1]>cut_pts and abs(etas[1])<cut_etas  and masses[1]>cut_masses_min and masses[1]<cut_masses_max
        jet2Flag = pts[2]>cut_pts and abs(etas[2])<cut_etas  and masses[2]>cut_masses_min and masses[2]<cut_masses_max


        if not (jet0Flag and jet1Flag and jet2Flag):
            continue

        nPass+=1

        jet0 = r.TLorentzVector()
        jet0.SetPtEtaPhiM(pts[0],etas[0],phis[0],masses[0])

        jet1 = r.TLorentzVector()
        jet1.SetPtEtaPhiM(pts[1],etas[1],phis[1],masses[1])

        jet2 = r.TLorentzVector()
        jet2.SetPtEtaPhiM(pts[2],etas[2],phis[2],masses[2])

        dijet01 = jet0 + jet1
        dijet02 = jet0 + jet2
        dijet12 = jet1 + jet2
        trijet012 = jet0 + jet1 + jet2

        hDijet01Masses.Fill(dijet01.M())
        hDijet02Masses.Fill(dijet02.M())
        hDijet12Masses.Fill(dijet12.M())
        hTrijet012Masses.Fill(trijet012.M())

    hCount = r.TH1F("evtCount","",2,0,2)
    hCount.SetBinContent(1,nGenEvents)
    hCount.SetBinContent(2,nPass)
    histos = [hDijet01Masses,hDijet02Masses,hDijet12Masses,hTrijet012Masses,hCount]

    saving(histos,output)   
    
def saving(histos,output):
    print("Saving {0}".format(output))
    f = r.TFile.Open(output,"RECREATE") #RECREATE izbriše stari output.root ako postoji, "UPDATE" se koristi ako želiš dodati histograme
    f.cd()
    for h in histos:
        h.Write()
    f.Close()

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-input', '--filename', help='list of file/singular file') 
    parser.add_argument('-output', '--file_location', help='output file location',default=False)
    args        = parser.parse_args()
    filename    = args.filename
    output      = args.file_location

    histogram(filename,output)