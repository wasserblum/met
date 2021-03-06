from BIOCLIC import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

def loadfile2(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()

    name = alldata[1]
    header = alldata[7] #Liste mit Flusskilometern - Distance from Mouth
    data = alldata[7:]  #Liste ab 8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  #Splitten der Listenelemente   split(":")  Seperator ":"

    return name, header, splitdata

#filename1 = "/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer_2/Temp_H2O.txt"
filename1 = "/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt"
name, header, thedata = hs_loader.loadfile(filename=filename1)

date_time = [i[0] for i in thedata] # Datum
hbs = [i[1] for i in thedata] # km 89
tbs = [i[10] for i in thedata] # km 84.5
sds = [i[19] for i in thedata] # km 80
rds = [i[41] for i in thedata] # km 69
oos = [i[49] for i in thedata] # km 65
uos = [i[54] for i in thedata] # km 62.5
uws = [i[57] for i in thedata] # km 61
j1s = [i[68] for i in thedata] # km 55.5
j2s = [i[69] for i in thedata] # km 55
j3s = [i[70] for i in thedata] # km 54.5
j4s = [i[76] for i in thedata] # km 51.5
z1s = [i[85] for i in thedata] # km 47
z2s = [i[86] for i in thedata] # km 46.5
bds = [i[89] for i in thedata] # km 45
wds = [i[97] for i in thedata] # km 41
bgs = [i[103] for i in thedata] # km 38

#filename2 = "/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_1.csv"
filename2 = "/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_20130725_0809_corr.csv"

name2, header2, thedata2 = loadfile2(filename=filename2)

hb = [i[1] for i in thedata2] # km 89
tb = [i[2] for i in thedata2] # km 84.5
sd = [i[3] for i in thedata2] # km 80
rd = [i[4] for i in thedata2] # km 69
oo = [i[5] for i in thedata2] # km 65
uo = [i[6] for i in thedata2] # km 62.5
uw = [i[7] for i in thedata2] # km 61
j1 = [i[8] for i in thedata2] # km 55.5
j2 = [i[9] for i in thedata2] # km 55
j3 = [i[10] for i in thedata2] # km 54.5
j4 = [i[11] for i in thedata2] # km 51.5
z1 = [i[12] for i in thedata2] # km 47
z2 = [i[13] for i in thedata2] # km 46.5
bd = [i[14] for i in thedata2] # km 45
wd = [i[15] for i in thedata2] # km 41
bg = [i[16] for i in thedata2] # km 38

fig = plt.figure()
#plt.plot(date_time, uws, color='red', lw=0.5, label='uw_s')
#plt.plot(date_time, uw, color='blue', lw=0.5, label='uw_m')

ax = fig.add_subplot(611)
ax.plot(date_time, tbs, color='red', lw=0.5, label='tb_s')
ax.plot(date_time, tb, color='blue', lw=0.5, label='tb_m')

ax = fig.add_subplot(612)
ax.plot(date_time, sds, color='red', lw=0.5, label='sd_s')
ax.plot(date_time, sd, color='blue', lw=0.5, label='sd_m')

ax = fig.add_subplot(613)
ax.plot(date_time, rds, color='red', lw=0.5, label='rd_s')
ax.plot(date_time, rd, color='blue', lw=0.5, label='rd_m')

ax = fig.add_subplot(614)
ax.plot(date_time, oos, color='red', lw=0.5, label='oo_s')
ax.plot(date_time, oo, color='blue', lw=0.5, label='oo_m')

ax = fig.add_subplot(615)
ax.plot(date_time, uos, color='red', lw=0.5, label='uo_s')
ax.plot(date_time, uo, color='blue', lw=0.5, label='uo_m')

ax = fig.add_subplot(616)
ax.plot(date_time, uws, color='red', lw=0.5, label='uw_s')
ax.plot(date_time, uw, color='blue', lw=0.5, label='uw_m')

#fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.ylabel('water temperature [degC]')
plt.legend()

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/UW_Validation_OrigConv_m.png')
plt.show()

fig = plt.figure()

ax = fig.add_subplot(511)
ax.plot(date_time, j1s, color='red', lw=0.5, label='j1_s')
ax.plot(date_time, j1, color='blue', lw=0.5, label='j1_m')

ax = fig.add_subplot(512)
ax.plot(date_time, j3s, color='red', lw=0.5, label='j3_s')
ax.plot(date_time, j3, color='blue', lw=0.5, label='j3_m')

ax = fig.add_subplot(513)
ax.plot(date_time, j4s, color='red', lw=0.5, label='j4_s')
ax.plot(date_time, j4, color='blue', lw=0.5, label='j4_m')

ax = fig.add_subplot(514)
ax.plot(date_time, z2s, color='red', lw=0.5, label='z2_s')
ax.plot(date_time, z2, color='blue', lw=0.5, label='z2_m')

ax = fig.add_subplot(515)
ax.plot(date_time, bgs, color='red', lw=0.5, label='bg_s')
ax.plot(date_time, bg, color='blue', lw=0.5, label='bg_m')

fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.ylabel('water temperature [degC]')
#plt.legend()

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/UW_Validation_OrigConv_m.png')
plt.show()