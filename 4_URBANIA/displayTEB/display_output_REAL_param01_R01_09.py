__author__ = 'lnx'
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# ---READING DATA---
#path = "/home/lnx/0_TEB/TEB/TEB_v1_1550/output/"
directory = "/home/lnx/0_TEB/TEB/3_testdata/REALtest/"
driver = "src_driver/driver.f90"
scenario1 = "R01"
scenario2 = "R02"
scenario3 = "R03"
scenario4 = "R04"
scenario5 = "R05"
scenario6 = "R06"
scenario7 = "R07"
scenario8 = "R08"
scenario9 = "R09"

path = directory+"output_"+scenario1+"/"
path2 = directory+"output_"+scenario2+"/"
path3 = directory+"output_"+scenario3+"/"
path4 = directory+"output_"+scenario4+"/"
path5 = directory+"output_"+scenario5+"/"
path6 = directory+"output_"+scenario6+"/"
path7 = directory+"output_"+scenario7+"/"
path8 = directory+"output_"+scenario8+"/"
path9 = directory+"output_"+scenario9+"/"


files =  ["H_TOWN.txt",
          "LE_TOWN.txt",
          "RN_TOWN.txt",
           "HVAC_COOL.txt",
          "HVAC_HEAT.txt",
           "U_CANYON.txt",
           "P_CANYON.txt",
           "Q_CANYON.txt",
           "T_CANYON.txt",
           "T_ROAD1.txt",
           "T_ROOF1.txt",
           "T_WALLA1.txt",
           "T_WALLB1.txt",
           "TI_BLD.txt",
           "UTCI_OUTSHADE.txt",
           "UTCI_OUTSUN.txt"]

data = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
datalabel = []
datalabel2 = []
datalabel3 = []
datalabel4 = []
datalabel5 = []
datalabel6 = []
datalabel7 = []
datalabel8 = []
datalabel9 = []

for f in files:
    filename = f
    name = f[:-4]
    filepath = path+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data.append(name)
    filepath = path2+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel2.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data2.append(name)
    filepath = path3+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel3.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data3.append(name)
    filepath = path4+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel4.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data4.append(name)
    filepath = path5+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel5.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data5.append(name)

    filepath = path6+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel6.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data6.append(name)
    filepath = path7+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel7.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data7.append(name)

    filepath = path8+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel8.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data8.append(name)

    filepath = path9+filename
    with open(filepath) as f:
        for line in f:
            reader = csv.reader(f)
            datalabel9.append(str(name))
            #print datalabel
            name = [row for row in reader]
            data9.append(name)

start = datetime.datetime(2016,8,4) #year: line 108, month: line 109, day line 110, hour: line 111, column37
#start = datetime.datetime(year,month,day) #year: line 108, month: line 109, day line 110, hour: line 111, column37
x = start + np.arange(3166) * datetime.timedelta(minutes=10)
#x = start + np.arange(nrtimestep) * datetime.timedelta(minutes=xstep)

#TODO: calculate threshold criteria (tropische naechte? sommertage, UTCI!)
#TODO: slice weeks of certain thresholds
#TODO: list important input settings of this simulation (H/W ratio, albedo,...)


#---CONVERSIONS---

tempcanyon = []
temproad1 = []
temproof1 = []
tempwall1 = []
tempwall2 = []
tempindoor = []

tempcanyon_2 = []
temproad1_2 = []
temproof1_2 = []
tempwall1_2 = []
tempwall2_2 = []
tempindoor_2 = []

tempcanyon_3 = []
temproad1_3 = []
temproof1_3 = []
tempwall1_3 = []
tempwall2_3 = []
tempindoor_3 = []

tempcanyon_4 = []
temproad1_4 = []
temproof1_4 = []
tempwall1_4 = []
tempwall2_4 = []
tempindoor_4 = []

tempcanyon_5 = []
tempcanyon_6 = []
tempcanyon_7 = []
tempcanyon_8 = []
tempcanyon_9 = []



def convert_celsius(list,output):
    for line in list:
        line = float(line[0])-273.15
        output.append(line)

for line in data[8]:
    line = float(line[0])-273.15
    tempcanyon.append(line)

for line in data2[8]:
    line = float(line[0])-273.15
    tempcanyon_2.append(line)

for line in data3[8]:
    line = float(line[0])-273.15
    tempcanyon_3.append(line)

for line in data4[8]:
    line = float(line[0])-273.15
    tempcanyon_4.append(line)


for line in data5[8]:
    line = float(line[0])-273.15
    tempcanyon_5.append(line)


for line in data6[8]:
    line = float(line[0])-273.15
    tempcanyon_6.append(line)


for line in data7[8]:
    line = float(line[0])-273.15
    tempcanyon_7.append(line)

for line in data8[8]:
    line = float(line[0])-273.15
    tempcanyon_8.append(line)

for line in data9[8]:
    line = float(line[0])-273.15
    tempcanyon_9.append(line)

convert_celsius(data[9],temproad1)
convert_celsius(data[10],temproof1)
convert_celsius(data[11],tempwall1)
convert_celsius(data[12],tempwall2)
convert_celsius(data[13],tempindoor)

#convert_celsius(data2[9],temproad1)


print (np.mean(tempcanyon))
print (np.max(tempcanyon))


fig = plt.figure()
#plt.title('temperature - canyon, Realnutzungskategorien' )
plt.plot(x, tempcanyon, linestyle='-', color = 'yellow', label = "1 - lockeres Wohn(misch)g.")# locker bebautes Wohn(misch)gebiet")
plt.plot(x, tempcanyon_2, linestyle='-', color = 'green', label = "2 - Gartenstadt")# Gartenstadt")
plt.plot(x, tempcanyon_3, linestyle='-', color = 'turquoise', label = "3 - dichtes Wohn(misch)g.")# dichtes Wohn(misch)gebiet")
plt.plot(x, tempcanyon_4, linestyle='-', color = 'blue', label = u"4 - großvolumiger solitärer Wohnb.")# grossvolumiger solitaerer Wohn(misch)bau")
plt.plot(x, tempcanyon_5, linestyle='-', color = 'violet', label = u"5 - Büro u. Verwaltung")# Buero- und Verwaltungsviertel")
plt.plot(x, tempcanyon_6, linestyle='-', color = 'pink', label = "6 - Handelsstrukturen")# solitaere Handelsstrukturen")
plt.plot(x, tempcanyon_7, linestyle='-', color = 'red', label = u"7 - Geschäfts-Kern-Mischg.")# Geschaefts- Kern- u. Mischgebiete")
plt.plot(x, tempcanyon_8, linestyle='-', color = 'orange', label = "8 - Mischnutzung - wenig dicht")# solitaere Handelsstrukturen")
plt.plot(x, tempcanyon_9, linestyle='-', color = 'brown', label = u"9 - Industrie, Großhandel, Lager.")# Geschaefts- Kern- u. Mischgebiete")

plt.grid(b=True, which='major', color='black', linestyle=':')
plt.grid(b=True, which='minor', color='r', linestyle=':')
plt.xlabel("time [UTC]", fontsize="large")
plt.ylabel(u"air temperature [°C]", fontsize="large")
plt.legend(loc=4, ncol=2, fontsize='large')
plt.show()

"""

fig = plt.figure()

ax = fig.add_subplot(411)
plt.title('canyon, %s' %(scenario))
plt.plot(x, data[5], linestyle='-', color = 'black', label = datalabel[8]) #wind
plt.ylabel("wind speed [m s-1]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(412)
plt.plot(x, data[6], linestyle='-', color = 'blue', label = datalabel[9]) #pressure
plt.ylabel("air pressure [Pa]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(413)
plt.plot(x, data[7], linestyle='-', color = 'red', label = datalabel[10]) #q
plt.ylabel("specific humidity [g g-2]")
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(414)
plt.plot(x, tempcanyon, linestyle='-', color = 'orange', label = datalabel[11]) #airtemp
plt.xlabel("time") #TODO:convert to days/hours
plt.ylabel("temperature [degC]")
#plt.legend(loc=4, ncol=3, fontsize='small')
plt.show()

#fig.savefig(/home/lnx/0_TEB/TEB/output_graphs/test.png)

"""