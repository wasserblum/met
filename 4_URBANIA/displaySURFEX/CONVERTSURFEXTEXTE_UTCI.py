#filename = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"

def loadfile(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    data = alldata[:]  #Liste ab [7:]8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())
    #print splitdata

    value = 0
    converted = []
    for i in splitdata:
        for j in i:
            value = (float(j[:8]) * 100)
            converted.append(value)
    #print converted
    return converted

#loadfile(filename)