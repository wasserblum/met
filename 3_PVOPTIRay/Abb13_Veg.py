# -*- coding: utf-8 -*-
__author__ = 'lnx'

import datetime

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile
from matplotlib.dates import DateFormatter

#S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N/2017_170/UTCI_OUTSHAD.TXT"
#S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N/2017_170NS/UTCI_OUTSHAD.TXT"
#S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N/2017_170WO/UTCI_OUTSHAD.TXT"
S200wo2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/UTCI_OUTSUN.TXT"
#S200nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N_25Grass/2017_170NS/UTCI_OUTSHAD.TXT"
S200woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_25Grass/2017_170171WO/UTCI_OUTSUN.TXT"
#S200nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N_25Trees/2017_170NS/UTCI_OUTSHAD.TXT"
S200woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_25Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
S200woGrass50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_50Grass/2017_170171WO/UTCI_OUTSUN.TXT"
S200woTrees50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_50Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
#S200woTrees100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_A_N_100Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
"""
S203 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170/UTCI_OUTSUN.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170NS/UTCI_OUTSUN.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170WO/UTCI_OUTSUN.TXT"
S203nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B_25Grass/2017_170NS/UTCI_OUTSUN.TXT"
S203woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B_25Grass/2017_170WO/UTCI_OUTSUN.TXT"
S203nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B_25Trees/2017_170NS/UTCI_OUTSUN.TXT"
S203woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B_25Trees/2017_170WO/UTCI_OUTSUN.TXT"

S200values = loadfile(S200)
S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S200NSgrassvalues = loadfile(S200nsGrass)
S200NStreesvalues = loadfile(S200nsTrees)
"""
S200wo2values = loadfile(S200wo2)
S200WOgrassvalues = loadfile(S200woGrass)
S200WOtreesvalues = loadfile(S200woTrees)
S200WOtrees50values = loadfile(S200woTrees50)
S200WOgrass50values = loadfile(S200woGrass50)

"""
S203values = loadfile(S203)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S203NSgrassvalues = loadfile(S203nsGrass)
S203WOgrassvalues = loadfile(S203woGrass)
S203NStreesvalues = loadfile(S203nsTrees)
S203WOtreesvalues = loadfile(S203woTrees)
"""
#diff200ns = np.copy(S200values)
#diff200wo = np.copy(S200values)
#diff200nsG = np.copy(S200values)
diff200woG = np.copy(S200wo2values)
diff200woG50 = np.copy(S200wo2values)
#diff200nsT = np.copy(S200values)
diff200woT = np.copy(S200wo2values)
diff200woT50 = np.copy(S200wo2values)
#diff203 = np.copy(S200values)
#diff203ns = np.copy(S200values)
#diff203wo= np.copy(S200values)
#diff203nsG = np.copy(S200values)
#diff203woG = np.copy(S200values)
#diff203nsT = np.copy(S200values)
#diff203woT = np.copy(S200values)

for i in range(len(S200wo2values)):
       #diff200ns[i] = S200NSvalues[i]-S200values[i]
       #diff200wo[i] = S200WOvalues[i]-S200values[i]
       #diff200nsG[i] = S200NSgrassvalues[i]-S200values[i]
       diff200woG[i] = S200WOgrassvalues[i]-S200wo2values[i]
       diff200woG50[i] = S200WOgrass50values[i]-S200wo2values[i]
       #diff200nsT[i] = S200NStreesvalues[i]-S200values[i]
       diff200woT[i] = S200WOtreesvalues[i]-S200wo2values[i]
       diff200woT50[i] = S200WOtrees50values[i]-S200wo2values[i]
       #diff203ns[i] = S203NSvalues[i]-S200values[i]
       #diff203wo[i] = S203WOvalues[i]-S200values[i]
       #diff203nsG[i] = S203NSgrassvalues[i]-S200values[i]
       #diff203woG[i] = S203WOgrassvalues[i]-S200values[i]
       #diff203nsT[i] = S203NStreesvalues[i]-S200values[i]
       #diff203woT[i] = S203WOtreesvalues[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
#numminutes= 1440
numminutes = 2880
timelist = []
xaxis=[]
for x in range (0, numminutes,10):
    moment = start + datetime.timedelta(minutes = x)
    hour = moment.hour
    timelist.append(moment)
    xaxis.append(hour)
xaxis = xaxis[:-1]
timelist = timelist[:-1]
#print timelist
#print len(S200values)
#print xaxis

fig1 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Vegetation,Asphalt,Canyon:HW1,20.6.2017")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
ax1.plot(timelist,S200wo2values, label="Asphalt", color="black")#,linestyle="dashed")
ax1.plot(timelist,S200WOgrassvalues, label=u"25% Wiese", color="green")#,linestyle="dashed")
ax1.plot(timelist,S200WOgrass50values, label=u"50% Wiese", color="green",linestyle=":")#,linestyle="dashed")
ax1.plot(timelist,S200WOtreesvalues, label=u"25% Bäume", color="blue")#,linestyle="dashed")
ax1.plot(timelist,S200WOtrees50values, label=u"50% Bäume", color="blue",linestyle=":")#,linestyle="dashed")

#ax1.plot(timelist,S200WOvalues, label="Asphalt", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#ax1.plot(timelist,S200NSgrassvalues, color="green",linestyle=":")
#ax1.plot(timelist,S200NStreesvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
#ax1.plot(timelist,S203WOvalues, label=r"$\alpha$ :0.56,0.56", color="turquoise",linestyle="dashed")
#ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
#ax2.plot(timelist,diff200nsG, color="green",linestyle=":")
ax2.plot(timelist,diff200woG, color="green")
ax2.plot(timelist,diff200woG50, color="green",linestyle=":")
#ax2.plot(timelist,diff200nsT, color="blue", linestyle=":")
ax2.plot(timelist,diff200woT, color="blue",)
ax2.plot(timelist,diff200woT50, color="blue",linestyle=":")
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
ax2.set_ylabel(r"$\Delta T_{a}$"u'UTCI[°C]')

ax1.legend(loc="lower right",fontsize='small')
ax1.set_ylabel(u'UTCI [°C]')
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()