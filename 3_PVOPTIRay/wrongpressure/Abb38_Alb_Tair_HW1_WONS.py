# -*- coding: utf-8 -*-
__author__ = 'lnx'

import datetime

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TCANYON.TXT"

S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TCANYON.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TCANYON.TXT"

S202ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/202_Kreuzung_A_A/2017_170171NS/TCANYON.TXT"
S202wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/202_Kreuzung_A_A/2017_170171WO/TCANYON.TXT"

S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170171NS/TCANYON.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170171WO/TCANYON.TXT"

S204ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170171NS/TCANYON.TXT"#
S204wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170171WO/TCANYON.TXT"#

S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170171NS/TCANYON.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170171WO/TCANYON.TXT"

S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
#S200whiteroofvalues = loadfile(S200_whiteroof)
#S200NSwhiteroofvalues = loadfile(S200ns_whiteroof)
#S200WOwhiteroofvalues = loadfile(S200wo_whiteroof)

S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)
S202NSvalues = loadfile(S202ns)
S202WOvalues = loadfile(S202wo)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S204NSvalues = loadfile(S204ns)
S204WOvalues = loadfile(S204wo)
S205NSvalues = loadfile(S205ns)
S205WOvalues = loadfile(S205wo)

#diff201 = np.copy(S200values)
#diff202 = np.copy(S200values)
#diff203 = np.copy(S200values)
#diff204 = np.copy(S200values)
#diff205 = np.copy(S200values)

#for i in range(len(S200values)):
#       diff201[i] = S201values[i]-S200values[i]
#       diff202[i] = S202values[i]-S200values[i]
#       diff203[i] = S203values[i]-S200values[i]
#       diff204[i] = S204values[i]-S200values[i]
#       diff205[i] = S205values[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
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

fig = plt.figure()
ax1 = fig.add_subplot(111)

#gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
#ax1 = plt.subplot(gs[0])
#ax2 = plt.subplot(gs[1])
ax1.set_title(u"Materialien,Straßenorientierung, Canyon:HW1, 19.6.2017")
#ax1.plot(timelist,S202values, label=u"Asphalt,dunkle Fassade", color="red") #u"α=0.13,0.13"
ax1.plot(timelist,S202WOvalues, label=r"$\alpha$ :0.13,0.13", color="red")#,linestyle="dashed")
ax1.plot(timelist,S202NSvalues, color="red",linestyle=":")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
#ax1.plot(timelist,S200WOwhiteroofvalues, label=r"$\alpha$ :0.13,0.20,0.80", color="black")#,linestyle="dashed")
#ax1.plot(timelist,S200NSwhiteroofvalues, color="pink",linestyle=":")
ax1.plot(timelist,S200WOvalues, label=r"$\alpha$ :0.13,0.20", color="orange")#,linestyle="dashed")
ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#ax1.plot(timelist,S201values, label="Beton,Putz", color="green")
ax1.plot(timelist,S201WOvalues, label=r"$\alpha$ :0.56,0.20", color="green")#,linestyle="dashed")
ax1.plot(timelist,S201NSvalues, color="green",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
ax1.plot(timelist,S203WOvalues, label=r"$\alpha$ :0.56,0.56", color="turquoise")#,linestyle="dashed")
ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
#ax1.plot(timelist,S204values, label=u"Beton,Weiß", color="blue")
ax1.plot(timelist,S204WOvalues, label=r"$\alpha$ :0.56,0.80", color="blue")#,linestyle="dashed")
ax1.plot(timelist,S204NSvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S205values, label=u"Weiß,Weiß", color="violet")
ax1.plot(timelist,S205WOvalues, label=r"$\alpha$ :0.80,0.80", color="violet")#,linestyle="dashed")
ax1.plot(timelist,S205NSvalues, color="violet",linestyle=":")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
#ax2.plot(timelist,diff201, label="Beton,Putz", color="green")
#ax2.plot(timelist,diff202, label="Asphalt,dunkle Fassade", color="red")
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
#ax2.plot(timelist,diff204, label=u"Beton,Weiß", color="blue")
#ax2.plot(timelist,diff205, label=u"Weiß,Weiß", color="violet")
#ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax1.set_xlabel('[UTC]')
plt.show()

exit()

fig2 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Einfluss PV/Boden, Platz - HW0.2, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax1.plot(timelist,S110values, label="Asphalt + 70%PV", color="orange")
#ax.plot(S113values, label="Asphalt + 100%PV", color="red")
ax1.plot(timelist,S111values, label="Beton + 70%PV", color="turquoise")
#ax.plot(S112values, label="Beton + 100%PV", color="blue")
#ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff110, label="Aspalt,PV", color="orange")
ax2.plot(timelist,diff111, label="Beton,PV", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()
plt.show()


fig3 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Einfluss PV/Boden, Kreuzung - HW1, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax1.plot(timelist,S210values, label="Asphalt,70%PV", color="orange")
#ax1.plot(timelist,S210NSvalues, label="Asphalt,70%PV,N-S", color="orange", linestyle="dashed" )
ax1.plot(timelist,S210WOvalues, label="Asphalt,70%PV,W-O", color="orange",linestyle=":")
#ax.plot(S213values, label="Asphalt + 100%PV", color="red")
#ax1.plot(timelist,S211values, label="Beton,70%PV", color="turquoise")
#ax1.plot(timelist,S211NSvalues, label="Beton,70%PV,N-S", color="turquoise", linestyle="dashed")
ax1.plot(timelist,S211WOvalues, label="Beton,70%PV,W-O", color="turquoise", linestyle=":")
#ax.plot(S212values, label="Beton + 100%PV", color="blue")
#ax1.plot(timelist,FORCvalues['Td'],label="Forcing (Dach)")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff210, label="Asphalt,PV", color="orange")
ax2.plot(timelist,diff211, label="Beton,PV", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Einfluss des Vegetation bei Asphalt")
#ax.plot(PVvalues, label="PV(canyon)")
#ax.plot(test, label="test")
ax.plot(STQvalues, label="keine Vegetation")
ax.plot(S2values, label="Wiese")
ax.plot(S3values, label="Park")
#ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax.set_ylabel(u'Lufftemperatur 2m [°C]')
ax.set_xlabel('[10min seit 0UTC]')
ax.legend(loc="upper left")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Einfluss des Vegetation bei Beton")
#ax.plot(PVvalues, label="PV(canyon)")
ax.plot(S4values, label="keine Vegetation")
ax.plot(S5values, label="Wiese")
ax.plot(S6values, label="Park")
ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax.set_ylabel(u'Lufftemperatur 2m [°C]')
ax.set_xlabel('[10min seit 0UTC]')
plt.legend(loc="upper left")
plt.show()


