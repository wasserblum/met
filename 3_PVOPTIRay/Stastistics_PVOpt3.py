import numpy as np
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile as loadfile_utci

#100_Platz_A_N","100_Platz_A_N","101_Platz_B_N","102_Platz_A_A","103_Platz_B_B",\
#"110_Platz_A_PV70","111_Platz_B_PV70",

simnames=["200_Can_A_N","200_Can_A_N_25Grass","200_Can_A_N_25Trees",\
"200_Can_A_N_iso","200_Can_A_N_PVroof", "200_Can_A_N_whiteroof",\
"201_Can_B_N","202_Can_A_A","203_Can_B_B","204_Can_B_W",\
"205_Can_W_W","210_Can_A_PV70", "211_Can_B_PV70", "200_Can_allwhite","200_Can_horwhite"]
simperiods=["2017_170171WO"]#,"2017_170171NS","2016_365366WO","2016_365366NS"]
temp= ["TCANYON","TWALLA1","TWALLB1","TRAD_SUN","TRAD_SHADE"] #"TROAD1",
utci=["UTCI_OUTSUN","UTCI_OUTSHAD"]

output = [[],[],[],[],[],[],[],[]]
for simname in simnames:
  for s in simperiods:
        path = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/" + simname + "/" + s + "/"
        tcounter=0
        ucounter=0
        print simname,s
        for i in range(len(temp)):
            name = "P"+temp[i]
            filepath = path + temp[i] + ".TXT"
            try:
                values = loadfile(filepath)
                print name, "max=",np.max(values[145:]),"min=",np.min(values[145:])
                #output[i+1+tcounter].append(np.max(values))
                #output[i+2+tcounter].append(np.min(values))
            except Exception:
                pass
            tcounter+=1
        for i in range(len(utci)):
            name= utci[i]
            filepath = path+utci[i]+".TXT"
            try:
                values = loadfile_utci(filepath)
                print name, "max=", np.max(values), "min=", np.min(values)
                output[i + 1 + ucounter].append(np.max(values))
            except Exception:
                pass
            ucounter+=1

exit()

simnames  = np.array(output[0])
per_ori  = np.array(output[1])
Ta_max = np.array(output[2])
Ta_min = np.array(output[3])
Twa_max = np.array(output[4])
Twa_min = np.array(output[5])
Twb_max = np.array(output[6])
Twb_min = np.array(output[7])




ab = np.zeros(simnames.size, dtype=[('var0', 'U32'),('var1', 'U32'), ('var2', float), ('var3', float),
              ('var4', float),('var5', float), ('var6', float),('var7', float)])
#print ab
ab['var0'] = simnames
ab['var1'] = per_ori
ab['var2'] = Ta_max
ab['var3'] = Ta_min
ab['var4'] = Twa_max
ab['var5'] = Twa_min
ab['var6'] = Twb_max
ab['var7'] = Twb_min

np.savetxt('test.txt', ab, fmt="%10s,%10s, %10.3f, %10.3f, %10.3f, %10.3f, %10.3f, %10.3f",
           header="simname,per_ori,Ta_max,Ta_min,Twa_max,Twa_min,Twb_max,Twb_min")

#with open('workfile.txt','w') as f:
#    np.savetxt(f,np.column_stack((output[0],output[1],output[2],output[3])),
#              fmt='%s,%32s,%2.2f,%2.2f',
#              header="simnam,dateORIE,Ta_max,Ta_min")
   # for slice_2d in b[1,1]:
#   np.savetxt(f,output,fmt='%10s;%10s;%3.2f;%3.2f',
#              header="simname;simperiod;Ta_max;Ta_min")

#f.close()


"""
        #os.chdir(path1)
        #print path1, print simname
        #files = os.listdir('./')
        #files = os.walk('./')
        #print files
        
        
        shutil.copytree(path1,path2)
		os.chdir(path1)
		with open('HeatSource_Control.csv','rb') as control :
			with open('fichier.csv','wb') as fichier :
				reader=csv.reader(control, delimiter=',', quotechar='|')
				writer=csv.writer(fichier,delimiter=',', quotechar='|')
				for row in reader :
					if row[0]=='2' :
						writer.writerow([row[0],row[1],name+"_049_"+s])
					elif row[0]=='4' :
						output=path2"outputfiles/"
						writer.writerow([row[0],row[1],output])
					elif row[0]=='5' :
						input=path2"inputfiles/"
						writer.writerow([row[0],row[1],input])
					else :
				writer.writerow(row)
		os.remove('HeatSource_Control.csv')
		os.rename('fichier.csv','HeatSource_Control.csv')
		execfile("Start_HS.py")
		shutil.rmtree(path1+"outputfiles/")
		shutil.copytree(path2+"ouputfiles/",path1+"outputfiles/")
		os.chdir("/home/heidi/hs")
		shutil.rmtree(path2)
"""