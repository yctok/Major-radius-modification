# -*- coding: utf-8 -*-

import numpy as np
import re

file ='C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2.equ'

with open(file) as f:
     datalist =f.readlines()

j= 17

while j< 43:
    string2 = datalist[j]
    gdata = re.findall('[-+]?\d+\.?\d+[eE]?[-+]\d+', string2)
    mylist =[]
    for ii in gdata:
        a = np.float64(ii) +np.float64(0.30000000)
        b = "{:.8E}".format(a)
        mylist.append(b)
    writelist = ' '.join(str(x)+"   " for x in mylist)
    datalist[j] = "\t" + writelist + "\n"
    j= j+ 1

file2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2_m.equ'
with open(file2,'w') as g:
    for i,line in enumerate(datalist,0):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        g.writelines(line)

w_file ='C:/Users/user/Documents/SOLPS data/simulation data/mast/vvfile.ogr'

with open(w_file) as wf:
     w_datalist = wf.readlines()

for m, k in enumerate(w_datalist):
#for m in range(10):
    string_w = w_datalist[m]
    w_data = re.findall('[-+]?\d+\.?\d+', string_w)  
    a = np.float64(w_data[0]) + np.float64(300.00000)
    a1 = "{: .5f}".format(a)
    b = np.float64(w_data[1])
    b1 = "{: .5f}".format(b)
    w_list =[]
    w_list.append(a1)
    w_list.append(b1)
    w_writelist = ' '.join(str(y)+ "\t  " for y in w_list)
    w_datalist[m] = "  " + w_writelist + "\n"
   
 
w_file2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/vvfile_m.ogr'
with open(w_file2,'w') as wg:
    for l,w_line in enumerate(w_datalist):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        wg.writelines(w_line)
