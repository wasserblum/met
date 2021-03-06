__author__ = 'lnx'
#DFS20 - V02085 - V702085 - V1002085 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF*0.85

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
WT_20a_2085_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V0_balance = WT_20a_2085_Sw_V0['80.000'][-24:].mean() + WT_20a_2085_Lw_V0['80.000'][-24:].mean()+ WT_20a_2085_Cv_V0['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V0['80.000'][-24:].mean()+ WT_20a_2085_Cd_V0['80.000'][-24:].mean()
V0_balance_s = "bal = %1.2f W m-2" %V0_balance

WT_20a_2085_Sw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V70_balance = WT_20a_2085_Sw_V70['80.000'][-24:].mean() + WT_20a_2085_Lw_V70['80.000'][-24:].mean()+ WT_20a_2085_Cv_V70['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V70['80.000'][-24:].mean()+ WT_20a_2085_Cd_V70['80.000'][-24:].mean()
V70_balance_s = "bal = %1.2f W m-2" %V70_balance

WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V100_balance = WT_20a_2085_Sw_V100['80.000'][-24:].mean() + WT_20a_2085_Lw_V100['80.000'][-24:].mean()+ WT_20a_2085_Cv_V100['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V100['80.000'][-24:].mean()+ WT_20a_2085_Cd_V100['80.000'][-24:].mean()
V100_balance_s = "bal = %1.2f W m-2" %V100_balance

WT_20a_2085_Sw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V0_085MLF_balance = WT_20a_2085_Sw_V0_085MLF['80.000'][-24:].mean() + WT_20a_2085_Lw_V0_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cv_V0_085MLF['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V0_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cd_V0_085MLF['80.000'][-24:].mean()
V0_085MLF_balance_s = "bal = %1.2f W m-2" %V0_085MLF_balance

WT_20a_2085_Sw_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V70_085MLF_balance = WT_20a_2085_Sw_V70_085MLF['80.000'][-24:].mean() + WT_20a_2085_Lw_V70_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cv_V70_085MLF['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V70_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cd_V70_085MLF['80.000'][-24:].mean()
V70_085MLF_balance_s = "bal = %1.2f W m-2" %V70_085MLF_balance

WT_20a_2085_Sw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

V100_085MLF_balance = WT_20a_2085_Sw_V100_085MLF['80.000'][-24:].mean() + WT_20a_2085_Lw_V100_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cv_V100_085MLF['80.000'][-24:].mean()+ \
             WT_20a_2085_Ev_V100_085MLF['80.000'][-24:].mean()+ WT_20a_2085_Cd_V100_085MLF['80.000'][-24:].mean()
V100_085MLF_balance_s = "bal = %1.2f W m-2" %V100_085MLF_balance


fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(231)
ax.set_title('V0, MLF')
ax.text(5, 500, V0_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V0['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax.set_ylabel('W m-2', fontsize='small')
#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')
#plt.show()

ax = fig.add_subplot(232)

##ALL SUBGRAPHS: DFS20, 2085/20a, last day of the episode!
#plt.ylim([-750,750])
ax.set_title('V70, MLF')
ax.text(5, 500, V70_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V70['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(233)
ax.set_title('V100, MLF')
ax.text(5, 500, V100_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V100['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])


ax = fig.add_subplot(234)
ax.set_title('V0, MLF -15')
ax.text(5, 500, V0_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V0_085MLF['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0_085MLF['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0_085MLF['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0_085MLF['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0_085MLF['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylabel('W m-2', fontsize='small')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])

ax = fig.add_subplot(235)
ax.set_title('V70, MLF -15')
ax.text(5, 500, V70_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V70_085MLF['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70_085MLF['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70_085MLF['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70_085MLF['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70_085MLF['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])

ax = fig.add_subplot(236)
ax.set_title('V100, MLF -15')
ax.text(5, 500, V100_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_2085_Sw_V100_085MLF['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100_085MLF['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100_085MLF['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100_085MLF['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100_085MLF['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])

plt.show()
