# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXNC_TXT import *
from scipy import stats
import sys
import matplotlib.gridspec as gridspec
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter

start = datetime(2015,7,18,0)
x = [start + timedelta(hours=i) for i in range(168)]
#print type(x[0])

'''
ZAMG - groundstations 

Coordinates: 
11034 Wien-Innere Stadt (85.5, 54.4, [16.366944444444446, 48.19833333333333])
11035 Wien-Hohe Warte (82.2, 69.7, [16.35638888888889, 48.24861111111111])
11036 Schwechat (147.3, 27.5, [16.56972222222222, 48.11027777777778])
11037 Gross-Enzersdorf (144.1, 54.8, [16.559166666666666, 48.19972222222222])
11040 Wien-Unterlaa (101.5, 32.0, [16.419444444444444, 48.125])
11042 Wien-Stammersdorf (97.2, 87.1, [16.405555555555555, 48.30583333333333])
11077 Brunn am Gebirge (55.9, 26.5, [16.27, 48.106944444444444])
11080 Wien-Mariabrunn (43.5, 57.0, [16.229444444444443, 48.206944444444446])
11090 Wien-Donaufeld (105.1, 72.3, [16.43138888888889, 48.257222222222225])

Parameters:
datum = 1_year_month_day
stdmin = minutes
tl = air temperature [1/10 degC]
k27 = global radiation [Watt/m2]
rf = rel Feuchte [%]
rr = Niederschlag 1/10 mm 10-Min-Summe
p = Luftdruck 1/10 hpascal
ff = Windstaerke [1/10 m/s] (Vektorielles 10 min Mittel,bezogen auf dd)
so = Sonnenscheindauer [seconds]
ts = 5cm air temperature
'''

ZAMGnames = {'11034': 'Wien-Innere Stadt', '11035':  "Wien-Hohe Warte", '11036': 'Schwechat',
             '11037':'Gross-Enzersdorf', '11040':'Wien-Unterlaa', '11042':'Wien-Stammersdorf',
             '11077':'Brunn am Gebirge', '11080':'Wien-Mariabrunn'}
#, '11090':'Wien-Donaufeld'} #missing data at Station Donaufeld 22.7. 2:50-12:30
ZAMGNo = ["11034","11035","11036","11037","11040","11042","11077","11080"]#,"11090"]

for i in ZAMGNo:
  ZAMGstation = "/home/lnx/METDATA/ZAMG_filled/tawes_" + i + "_year_2015.txt"
  ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
  Day1 = ZAMGdata.loc[ZAMGdata['datum'] == 1150717] #cut episode
  Day1 = Day1.loc[ZAMGdata['stdmin'] >= 1800] #cut episode
  Day2 = ZAMGdata.loc[ZAMGdata['datum'] == 1150718] #cut episode
  Day3 = ZAMGdata.loc[ZAMGdata['datum'] == 1150719] #cut episode
  Day4 = ZAMGdata.loc[ZAMGdata['datum'] == 1150720] #cut episode
  Day5 = ZAMGdata.loc[ZAMGdata['datum'] == 1150721] #cut episode
  Day6 = ZAMGdata.loc[ZAMGdata['datum'] == 1150722] #cut episode
  Day7 = ZAMGdata.loc[ZAMGdata['datum'] == 1150723] #cut episode
  Day8 = ZAMGdata.loc[ZAMGdata['datum'] == 1150724] #cut episode
  Day9 = ZAMGdata.loc[ZAMGdata['datum'] == 1150725] #cut episode
  Day10 = ZAMGdata.loc[ZAMGdata['datum'] == 1150726] #cut episode
  Day11 = ZAMGdata.loc[ZAMGdata['datum'] == 1150727] #cut episode
  Day12 = ZAMGdata.loc[ZAMGdata['datum'] == 1150728] #cut episode

  ZAMG_episode = pd.concat([Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12], axis=0)
  #extract date:
  date = ZAMG_episode['datum'].iloc[0]
  date1 = str(date).split()
  date_start = date1[0][5:7] +"." +date1[0][3:5] +".20"+ date1[0][1:3]
  ZAMG_TA = ZAMG_episode['tl']/10 #extract 2M air temperature and bring to °C
  ZAMG_TA_hourly = ZAMG_TA[0::6]  #s[i:j:k]  slice of s from i to j with step k

  '''WRF online and SURFEX offline runs ... HERE THE CORRECT FILEPATHS NEED TO BE CHECKED'''
  SURFEX_S0 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/" \
              "hapex/S0_FORC_WRF_333_STQ_long/T2M_" + i +".txt"
  SURFEX_S12 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/" \
             "hapex/S12_FORC_WRF_333_STQ_2DURBPARAM_long_corr/T2M_" + i +".txt"

  SURFEXdataS0 = loadfile1(SURFEX_S0)
  SURFEXdataS12 = loadfile1(SURFEX_S12)
  FORCING = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/Urbania/FORCING_WRF1/T2M_"+i+".txt"
  WRFdata = loadfile3(FORCING)

  '''convert to numpy array and bring to same filesize'''
  ZAMG_heatdays = np.array(ZAMG_TA_hourly[8:176])# np.vstack((np.array(ZAMG_TA_hourly[13:109]),np.array(ZAMG_TA_hourly[133:-98])))  #[13:]
  WRFdata_heatdays = np.array(WRFdata[8:176])
  SURFEXdataS0_heatdays = np.array(SURFEXdataS0[8:176])
  SURFEXdataS12_heatdays = np.array(SURFEXdataS12[8:176])
  #print type(ZAMG_heatdays), len(ZAMG_heatdays), ZAMG_heatdays[0]
  #exit()

  '''calculation of bias'''
  Bias_Forc_i = np.average(WRFdata_heatdays-ZAMG_heatdays)
  Bias_WRF_S0_i = np.average(SURFEXdataS0_heatdays-ZAMG_heatdays)
  Bias_WRF_S12_i = np.average(SURFEXdataS12_heatdays-ZAMG_heatdays)
  print i, Bias_Forc_i, Bias_WRF_S0_i, Bias_WRF_S12_i

  '''calculation of Regression coefficients'''
  #print stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays, axis=0)
  R2_Forc_i = (stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays))[0] ** 2
  R2_WRF_S0_i = (stats.spearmanr(ZAMG_heatdays, SURFEXdataS0_heatdays))[0] ** 2
  R2_WRF_S12_i = (stats.spearmanr(ZAMG_heatdays, SURFEXdataS12_heatdays))[0] ** 2
  print i, R2_Forc_i, R2_WRF_S0_i, R2_WRF_S12_i

  try:
    '''
    Plotting
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(ZAMG_heatdays, color='black', label=u"Ground station")
    ax1.plot(WRFdata_heatdays, color='blue', label="WRF(US)")  #31
    ax1.plot(SURFEXdataS0_heatdays, color='red', label="WRF/S(EC)")
    ax1.plot(SURFEXdataS12_heatdays, color='orange', label="WRF/S(PM)")
    ax1.set_xlabel("hours[UTC]")
    ax1.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax1.legend(loc='upper right')
    ax1.set_xlim(0, 168)
    ax1.set_ylim(19, 40)
    #myFmt = DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig.autofmt_xdate()

    ax2 = fig.add_subplot(122)
    plt.scatter(ZAMG_heatdays, WRFdata_heatdays, color='blue')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    plt.scatter(ZAMG_heatdays, SURFEXdataS0_heatdays, color='red')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_S0_i, Bias_WRF_S0_i)))
    plt.scatter(ZAMG_heatdays, SURFEXdataS12_heatdays, color='orange')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_S12_i, Bias_WRF_S12_i)))
    ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax2.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax2.legend(loc='upper left')
    plt.suptitle(ZAMGnames[i] + ", 18 - 24 July 2015", size="large")#+"2m air temperature"))
    #plt.suptitle(ZAMGnames[i] + ", 17 - 27 July 2015", size="large")#+"2m air temperature"))
    plt.show()
  except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass



