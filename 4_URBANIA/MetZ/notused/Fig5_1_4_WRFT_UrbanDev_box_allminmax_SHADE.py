# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_ref = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
file_alb = '/media/lnx/Norskehavet/OFFLINE/2069ALB/TEB_DIAGNOSTICS.OUT.nc'
file_iso = '/media/lnx/Norskehavet/OFFLINE/2069ISO/TEB_DIAGNOSTICS.OUT.nc'
file_grr = '/media/lnx/Norskehavet/OFFLINE/2069GRR/TEB_DIAGNOSTICS.OUT.nc'
file_den = '/media/lnx/Norskehavet/OFFLINE/2069DEN/TEB_DIAGNOSTICS.OUT.nc'
file_pvr = '/media/lnx/Norskehavet/OFFLINE/2069PVR/TEB_DIAGNOSTICS.OUT.nc'
file_spr = '/media/lnx/Norskehavet/OFFLINE/2069SPR/TEB_DIAGNOSTICS.OUT.nc'
file_opt = '/media/lnx/Norskehavet/OFFLINE/2069OPT/dx345corr/TEB_DIAGNOSTICS.OUT.nc'
#dimensions(sizes): xx(174), yy(135), time(174) 1.7.2069 18h - 8.7.23h

f_ref2015 = Dataset(file_ref2015, mode='r')
f_ref = Dataset(file_ref, mode='r')
f_alb = Dataset(file_alb, mode='r')
f_iso = Dataset(file_iso, mode='r')
f_grr = Dataset(file_grr, mode='r')
f_den = Dataset(file_den, mode='r')
f_pvr = Dataset(file_pvr, mode='r')
f_spr = Dataset(file_spr, mode='r')
f_opt = Dataset(file_opt, mode='r')
var_units = f_ref.variables['UTCI_OUTSHAD'].units

'''cut for subregions'''
var_ref = f_ref.variables['UTCI_OUTSHAD']

var_ref2015_ce = f_ref2015.variables['UTCI_OUTSHAD'][:,57:66,128:137] #[:,50:59,80:89]
var_ref_ce = f_ref.variables['UTCI_OUTSHAD'][:,57:66,128:137] #[:,50:59,80:89]
var_alb_ce = f_alb.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_iso_ce = f_iso.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_den_ce = f_den.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_grr_ce = f_grr.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_pvr_ce = f_pvr.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_spr_ce = f_spr.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
var_opt_ce = f_opt.variables['UTCI_OUTSHAD'][:,50:59,80:89] #[:,50:59,80:89]
print var_ref_ce.shape

#NO = [:,73:82,89:98]
#CE = [:,50:59,80:89]
#RU = [:,57:66,128:137]
#SA = [:,58:67,109:118]
#SE = [:,37:46,99:108]
#SX = [:,24:33,75:84]
#SI = [:,31:40,68:77]
#VW = [:,47:56,64:73]
#WE = [:,62:71,73:82]

utci_ref_ce_max=[]
utci_ref_ce_min=[]
for i in range(9):
    for j in range(9):
        add = var_ref_ce[150:174,i,j].max()
        if add!=nan:
          utci_ref_ce_max.append(add)
        else:
          utci_ref_ce_max.append(0)
        add2 = var_ref_ce[150:174, i, j].min()
        if add2 != nan:
            utci_ref_ce_min.append(add2)
        else:
            utci_ref_ce_min.append(0)

utci_alb_ce_max=[]
utci_alb_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_alb_ce[150:174,i,j].max())
        if add!=nan:
          utci_alb_ce_max.append(add)
        else:
          utci_alb_ce_max.append(0)
        add2 = var_alb_ce[150:174, i, j].min()
        if add2 != nan:
          utci_alb_ce_min.append(add2)
        else:
          utci_alb_ce_min.append(0)

utci_iso_ce_max=[]
utci_iso_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_iso_ce[150:174,i,j].max())
        if add!=nan:
          utci_iso_ce_max.append(add)
        else:
          utci_iso_ce_max.append(0)
        add2 = var_iso_ce[150:174, i, j].min()
        if add2 != nan:
          utci_iso_ce_min.append(add2)
        else:
          utci_iso_ce_min.append(0)

utci_den_ce_max=[]
utci_den_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_den_ce[150:174,i,j].max())
        if add!=nan:
          utci_den_ce_max.append(add)
        else:
          utci_den_ce_max.append(0)
        add2 = var_den_ce[150:174, i, j].min()
        if add2 != nan:
          utci_den_ce_min.append(add2)
        else:
          utci_den_ce_min.append(0)

utci_grr_ce_max=[]
utci_grr_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_grr_ce[150:174,i,j].max())
        if add!=nan:
          utci_grr_ce_max.append(add)
        else:
          utci_grr_ce_max.append(0)
        add2 = var_grr_ce[150:174, i, j].min()
        if add2 != nan:
          utci_grr_ce_min.append(add2)
        else:
          utci_grr_ce_min.append(0)

utci_pvr_ce_max=[]
utci_pvr_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_pvr_ce[150:174,i,j].max())
        if add!=nan:
          utci_pvr_ce_max.append(add)
        else:
          utci_pvr_ce_max.append(0)
        add2 = var_pvr_ce[150:174, i, j].min()
        if add2 != nan:
          utci_pvr_ce_min.append(add2)
        else:
          utci_pvr_ce_min.append(0)

utci_spr_ce_max=[]
utci_spr_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_spr_ce[150:174,i,j].max())
        if add!=nan:
          utci_spr_ce_max.append(add)
        else:
          utci_spr_ce_max.append(0)
        add2 = var_spr_ce[150:174, i, j].min()
        if add2 != nan:
          utci_spr_ce_min.append(add2)
        else:
          utci_spr_ce_min.append(0)

utci_opt_ce_max=[]
utci_opt_ce_min=[]
for i in range(9):
    for j in range(9):
        add = (var_opt_ce[150:174,i,j].max())
        if add!=nan:
          utci_opt_ce_max.append(add)
        else:
          utci_opt_ce_max.append(0)
        add2 = var_opt_ce[150:174, i, j].min()
        if add2 != nan:
          utci_opt_ce_min.append(add2)
        else:
          utci_opt_ce_min.append(0)

f_ref2015.close()
f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
f_spr.close()
f_opt.close()

print "MAX"
ref_max = list(filter(lambda x: x!=0, utci_ref_ce_max))
#print "REF=", np.mean(ref_max)

print "REF2069_md=", np.median(utci_ref_ce_max)
print "REF2069_mn=", np.mean(ref_max)
print "ALBdiff=", np.mean(list(filter(lambda x: x!=0, utci_alb_ce_max)))-np.mean(ref_max)
print "ISOdiff=", np.mean(list(filter(lambda x: x!=0, utci_iso_ce_max)))-np.mean(ref_max)
print "DENdiff=", np.mean(list(filter(lambda x: x!=0, utci_den_ce_max)))-np.mean(ref_max)
print "GRRdiff=", np.mean(list(filter(lambda x: x!=0, utci_grr_ce_max)))-np.mean(ref_max)
print "PVRdiff=", np.mean(list(filter(lambda x: x!=0, utci_pvr_ce_max)))-np.mean(ref_max)
print "SPRdiff=", np.mean(list(filter(lambda x: x!=0, utci_spr_ce_max)))-np.mean(ref_max)
print "OPTdiff=", np.mean(list(filter(lambda x: x!=0, utci_opt_ce_max)))-np.mean(ref_max)

print "\nMIN"
ref_min = list(filter(lambda x: x!=0, utci_ref_ce_min))
print "REF_md=", np.median(ref_min)
print "REF_mn=", np.mean(ref_min)
print "ALBdiff=", np.mean(list(filter(lambda x: x!=0, utci_alb_ce_min)))-np.mean(ref_min)
print "ISOdiff=", np.mean(list(filter(lambda x: x!=0, utci_iso_ce_min)))-np.mean(ref_min)
print "DENdiff=", np.mean(list(filter(lambda x: x!=0, utci_den_ce_min)))-np.mean(ref_min)
print "GRRdiff=", np.mean(list(filter(lambda x: x!=0, utci_grr_ce_min)))-np.mean(ref_min)
print "PVRdiff=", np.mean(list(filter(lambda x: x!=0, utci_pvr_ce_min)))-np.mean(ref_min)
print "SPRdiff=", np.mean(list(filter(lambda x: x!=0, utci_spr_ce_min)))-np.mean(ref_min)
print "OPTdiff=", np.mean(list(filter(lambda x: x!=0, utci_opt_ce_min)))-np.mean(ref_min)

exit()

UTCI_CE_max= transpose([utci_ref_ce_max,utci_alb_ce_max,
utci_iso_ce_max,utci_den_ce_max,utci_grr_ce_max, utci_pvr_ce_max])

UTCI_CE_min = transpose([utci_ref_ce_min,utci_alb_ce_min,
utci_iso_ce_min, utci_den_ce_min, utci_grr_ce_min, utci_pvr_ce_min])

#TairCE_filtered = TairCE[~np.isnan(TairCE)]
labels = ["REF","ALB","ISO","DEN","GRR","PVR"]
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html
#The box extends from the lower (Q1) to the upper (Q3) quartile values of data, with a line at the median
#The whiskers extend from the box to show the range of data, default=1.5 ->   Q1-whis*IQR, Q3+whis*IQR (interquartiles range)
#whis=[5,95]  Set whiskers to percentiles

fig2, axs = plt.subplots(nrows=1, ncols=2)#, figsize=(9, 4))
#fig2.suptitle("daily maxima and minima, averaged over center for 8 Jul 2069")
axs[0].boxplot(UTCI_CE_max, notch=True, labels=labels, showfliers=False)#, whis=[5,95])
axs[0].set_ylabel(r"$UTCI Shade$"u'[°C]')
axs[0].set_xlabel("MAX")
#axs[0].set_ylim([42,55])
axs[0].set_ylim([43,47])

#axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[1].boxplot(UTCI_CE_min,  notch=True, labels=labels, showfliers=False)#True,  whis=[5,95])
axs[1].set_xlabel("MIN")
#axs[1].set_ylim([25,37])
axs[1].set_ylim([27,31])
#axs[1].set_yticklabels([])

plt.show()


