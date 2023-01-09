import ROOT as r
from argparse import ArgumentParser
import json

def get_numbers(filenames):
    f = r.TFile.Open(filename)

    
    hist = f.evtCount

    nbins = hist.GetNbinsX()

    num_events = []
    #citanje broja događaja
    for i in range(1, nbins+1):
        bin_val = hist.GetBinContent(i)

        num_events.append(bin_val)

    #citanje udarnih preseka
    with open("udarni_presjeci.json", "r") as presjeci:
           presjeci_dict = json.load(presjeci)

    lista_presjeka = list(presjeci_dict.values())

    #citanje udarnih preseka
    with open("luminozitet.json", "r") as luminozitet:
           luminozitet_dict = json.load(luminozitet)

    lum = list(luminozitet_dict.values())[0]

    #otvranje json datoteke u koju se spremaju vrijednosti normalizacije
    with open("norma.json", "r") as nora:
           norma_dict = json.load(nora)

    #racuna normalizacije
    if "1000" in filename:
    	udarni_presjek =  lista_presjeka[0]

    	norma = lum * 1000 * udarni_presjek/num_events[0]

    	norma_dict.update({"QCD1000": norma})

    elif "1500" in filename:
    	udarni_presjek =  lista_presjeka[1]

    	norma = lum * 1000 * udarni_presjek/num_events[0]

    	print(norma)

    	norma_dict.update({"QCD1500": norma})

    elif "2000" in filename:
    	udarni_presjek =  lista_presjeka[2]

    	norma = lum * 1000 * udarni_presjek/num_events[0]

    	print(norma)

    	norma_dict.update({"QCD2000": norma})

    else: 
    	udarni_presjek =  lista_presjeka[3]

    	norma = lum * 1000 * udarni_presjek/num_events[0]

    	print(norma)

    	norma_dict.update({"QCD700": norma})

    print(norma_dict) #za provjeru

    
    with open("norma.json", "w") as nora:
        json.dump(norma_dict, nora, indent=1)






if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-f:', '--filename', help='list of file/singular file') 
    args        = parser.parse_args()
    filename    = args.filename

    get_numbers(filename)