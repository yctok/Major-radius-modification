# -*- coding: utf-8 -*-

import numpy as np
import re


simu_loc = 'C:/Users/ychuang/Documents/SOLPS_data/simulation_data/mast/027205'
simu_case = 'AD3D'
file_dir = '{}/{}/baserun'.format(simu_loc, simu_case)
equfile_dir = '{}/g027205_0275.X2.equ'.format(file_dir)




shift_value = 0.55



# file = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2.equ'

with open(equfile_dir) as f:
     datalist = f.readlines()


def line_index_finder(file_lines):
    
    index_dic = {}
    
    for j, lines in enumerate(file_lines):
    
        if 'r(1:jm);' in lines:
            print(j)
            
            index_dic['r'] = j+1
        
        elif 'z(1:km);' in lines:
            print(j)
            
            index_dic['z'] = j-1
        
        elif 'rtf' in lines:
            print(j)
            
            index_dic['Btaxis'] = j
        
        else:
            pass
    
    return index_dic


index_dic = line_index_finder(datalist)
print(index_dic)


bt = index_dic['Btaxis']
text = datalist[bt]
number = re.findall('[-+]?\d+\.\d+', text)
print(number)



j= index_dic['r']

while j< index_dic['z']:
    string2 = datalist[j]
    gdata = re.findall('[-+]?\d+\.?\d+[eE]?[-+]\d+', string2)
    mylist =[]
    for ii in gdata:
        a = np.float64(ii) +np.float64(shift_value)
        b = "{:.8E}".format(a)
        mylist.append(b)
    writelist = ' '.join(str(x)+"   " for x in mylist)
    datalist[j] = '    ' + writelist + "\n"
    j= j+ 1

m_equfile = '{}/g027205.00275.X2_m.equ'.format(file_dir)




with open(m_equfile,'w') as g:
    for i,line in enumerate(datalist,0):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        g.writelines(line)


def replacetext(search_text, replace_text):
    with open(m_equfile, "r+") as f:
        file_content = f.read()
        file_content = re.sub(search_text, replace_text, file_content)
        f.seek(0)
        f.write(file_content)
        f.truncate()
        return "Text replaced"

search_text = number[0]

shift_axis = np.float64(number[0]) + shift_value
print(shift_axis)

replace_text = '{:.17f}'.format(shift_axis)
print(replacetext(search_text = search_text, replace_text = replace_text))




vessel_file = '{}/vvfile.ogr'.format(file_dir)



with open(vessel_file) as wf:
     w_datalist = wf.readlines()


vessel_value = shift_value*1000

for m, k in enumerate(w_datalist):
#for m in range(10):
    string_w = w_datalist[m]
    w_data = re.findall('[-+]?\d+\.?\d+', string_w)  
    a = np.float64(w_data[0]) + np.float64(vessel_value)
    a1 = "{: .5f}".format(a)
    b = np.float64(w_data[1])
    b1 = "{: .5f}".format(b)
    w_list =[]
    w_list.append(a1)
    w_list.append(b1)
    w_writelist = ' '.join(str(y)+ "\t  " for y in w_list)
    w_datalist[m] = "  " + w_writelist + "\n"
   


m_vesselfile = '{}/vvfile_m.ogr'.format(file_dir)


with open(m_vesselfile,'w') as wg:
    for l,w_line in enumerate(w_datalist):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        wg.writelines(w_line)
