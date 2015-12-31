# coding=utf-8
from Hs_scripts import hs9_loader
from Hs_scripts import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata = hs9_loader.loadfile(filename=filename)

date_time = [i[0] for i in thedata]
thedata_withouttime = [i[1:] for i in thedata]

Rkm =  [93.0,92.5,92.0,91.5,91.0,90.5,90.0,89.5,89.0,88.5,88.0,87.5,87.0,86.5,86.0,85.5,85.0,84.5,84.0,
        83.5,83.0,82.5,82.0,81.5,81.0,80.5,80.0,79.5,79.0,78.5,78.0,77.5,77.0,76.5,76.0,75.5,75.0,74.5,74.0,73.5,73.0,
        72.5,72.0,71.5,71.0,70.5,70.0,69.5,69.0,68.5,68.0,67.5,67.0,66.5,66.0,65.5,65.0,64.5,64.0,63.5,63.0,62.5,62.0,
        61.5,61.0,60.5,60.0,59.5,59.0,58.5,58.0,57.5,57.0,56.5,56.0,55.5,55.0,54.5,54.0,53.5,53.0,52.5,52.0,51.5,51.0,
        50.5,50.0,49.5,49.0,48.5,48.0,47.5,47.0,46.5,46.0,45.5,45.0,44.5,44.0,43.5,43.0,42.5,42.0,41.5,41.0,40.5,40.0,
        39.5,39.0,38.5,38.0,37.5,37.0,36.5,36.0,35.5,35.0,34.5,34.000,33.5,33.0,32.5,32.0,31.5,31.0,30.5,30.0,29.5,29.0,
        28.5,28.0,27.5,27.0,26.5,26.0,25.5,25.0,24.5,24.0,23.5,23.0,22.5,22.0,21.5,21.0,20.5,20.0,19.5,19.0,18.5,18.0,
        17.5,17.0,16.5,16.0,15.5,15.0,14.5,14.0,13.5,13.0,12.5,12.0,11.5,11.0,10.5,10.0,9.5,9.0,8.5,8.0,7.5]

# T6h = thedata_withouttime[6] #1.Juli 2013 minimum of km93
# T14h = thedata_withouttime[14] #1.Juli 2013 maximum of km7.5
# T17h = thedata_withouttime[17] #1.Juli 2013 maximum of km93
# T25h = thedata_withouttime[25] #2.Juli 2013 minimum of km7.5

T6h = thedata_withouttime[6]
T9h = thedata_withouttime[9]
T12h = thedata_withouttime[12]
T15h = thedata_withouttime[15]
T18h = thedata_withouttime[18]
T21h = thedata_withouttime[21]
T24h = thedata_withouttime[24]
T27h = thedata_withouttime[27]

fig = plt.figure()

plt.title('1.July 2013 6am - 2.July 3am')
plt.plot(Rkm, T6h, color='blue', lw=0.5, label='6h')
plt.plot(Rkm, T9h, color='lightblue', lw=0.5, label='9h')
plt.plot(Rkm, T12h, color='turquoise', lw =0.5,label='12h')
plt.plot(Rkm, T15h, color='lightgreen', lw =0.5, label='15h')
plt.plot(Rkm, T18h, color='green', lw =0.5, label='18h')
plt.plot(Rkm, T21h, color='yellow', lw =0.5, label='21h')
plt.plot(Rkm, T24h, color='orange', lw =0.5, label='24h')
plt.plot(Rkm, T27h, color='red', lw =0.5, label='27h')

plt.ylabel('water temperature[degC]')
plt.xlabel('river distance from mouth [km]')

plt.legend(bbox_to_anchor=(1.00, 1), loc=2, borderaxespad=0.)

plt.show()