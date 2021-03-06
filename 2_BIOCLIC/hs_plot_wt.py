from BIOCLIC import hs_loader
from BIOCLIC import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\win32\Test\inputfiles\Temp_H2O.txt"
thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata

date_time = [i[0] for i in thedata]
x1 = [i[1] for i in thedata]
x2 = [i[2] for i in thedata]
x3 = [i[3] for i in thedata]
x4 = [i[4] for i in thedata]

filename = "C:\heatsource900b5_339\win32\Test\inputfiles\Temp_H2O.txt"
thedata2 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata2

#date_time = [i[0] for i in thedata2]
b1 = [i[1] for i in thedata2]
b2= [i[2] for i in thedata2]
b3 = [i[3] for i in thedata2]
b4 = [i[4] for i in thedata2]

filename = "C:\heatsource900b5_339\win32\Test\inputfiles\Temp_H2O.txt"
thedata3 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata3

#date_time = [i[0] for i in thedata3]
c1 = [i[1] for i in thedata3]
c2 = [i[2] for i in thedata3]
c3 = [i[3] for i in thedata3]
c4 = [i[4] for i in thedata3]

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c10_v01_f3/Temp_H2O.txt"
thedata4 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata4

#date_time = [i[0] for i in thedata4]
d1 = [i[1] for i in thedata4]
d2 = [i[2] for i in thedata4]
d3 = [i[3] for i in thedata4]
d4 = [i[4] for i in thedata4]

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/Continousdata_HS808_20130415.txt"
thedata5 = hs_cdataloader.loadfile(filename=filename)
print 'loaded: ', thedata5

date_time2 = [i[0] for i in thedata5]
e1 = [i[3] for i in thedata5]

matches = list(set(date_time) & set(date_time2))
matches.sort()
for m in matches:
    print(m)


eld = []
for d in matches:
    index = date_time2.index(d)
    eld.append(thedata5[index][2])
    print index

print eld
e1 = [i[3] for i in thedata5]

fig = plt.figure()


ax = fig.add_subplot(221)
ax.plot(date_time, x1, color='red', lw=0.5)
ax.plot(date_time, x2, color='darkred', lw=0.5)
ax.plot(date_time, x3, color='violet', lw=0.5)
ax.plot(date_time, x4, color='darkblue', lw=0.5)
ax.plot(date_time, eld, color='black', lw=0.5)
#ax.plot(graphiken['RO'][12], color='blue', lw=0.5)
#plt.axis([0, 15, -15, 15])
#plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
#plt.text(20, 18, 'I', fontsize=20)
plt.ylabel('water temperature[degC], cloudiness = 0%')
#plt.ylim(-15,15)

ax = fig.add_subplot(222)
ax.plot(date_time, b1, color='red', lw=0.5)
ax.plot(date_time, b2, color='darkred', lw=0.5)
ax.plot(date_time, b3, color='violet', lw=0.5)
ax.plot(date_time, b4, color='darkblue', lw=0.5)
ax.plot(date_time, eld, color='black', lw=0.5)
# plt.text(20, 18, 'II', fontsize=20)
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.axis([1, 23, 5, 20])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


ax = fig.add_subplot(223)
ax.plot(date_time, c1, color='red', lw=0.5)
ax.plot(date_time, c2, color='darkred', lw=0.5)
ax.plot(date_time, c3, color='violet', lw=0.5)
ax.plot(date_time, c4, color='darkblue', lw=0.5)
ax.plot(date_time, eld, color='black', lw=0.5)
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'III', fontsize=20)
plt.ylabel('cloudiness = 100%')
plt.xlabel('time[h], flow = 0.5cms')

ax = fig.add_subplot(224)
ax.plot(date_time, d1, color='red', lw=0.5, label='0.65')
ax.plot(date_time, d2, color='darkred', lw=0.5, label='0.40')
ax.plot(date_time, d3, color='violet', lw=0.5, label='0.15')
ax.plot(date_time, d4, color='darkblue', lw=0.5, label='0.00')
ax.plot(date_time, eld, color='black', lw=0.5, label='meas')
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'IV', fontsize=20)
fig.autofmt_xdate()
plt.xlabel('time[h], flow = 3cms')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="km")


#plt.legend()
# fig.savefig('albedo.png')
plt.show()