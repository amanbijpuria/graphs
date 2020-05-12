all_files = []
to_address=[]
each_part_file = {}
import glob
import os
import re
import networkx as nx
import matplotlib.pyplot as plt
    
#path = r'C:\Users\AMAN\Downloads\data\files\*'
for filename in glob.glob(os.path.join(os.path.expanduser('~'),'Downloads','data','files','*')):
        file = open(filename).readlines()
        for i in file:
            fields = i.split(":")
            #print(fields)
            if fields[0]== 'From' :
                each_part_file={}
                each_part_file[fields[0]] = fields[1].strip()
            if fields[0] =='To' :
                each_part_file[fields[0]] = re.split('[;,]', fields[1].strip())
            #print(each_part_file)    
            if (('From' in each_part_file) & ('To' in each_part_file)):
                all_files.append(each_part_file)
                each_part_file={}
                break
        
set_1=set()
set_2=set()
for i in all_files:
    set_1.add(i['From'].strip())
    for j in set(i['To']) :
        set_1.add(j)

lst = list(set_1)
new_lst=[]
while("" in lst) : 
    lst.remove("")

for i in lst:
    new_lst.append(i.strip())
    
new_relation={}
lst_3=[]
for i in new_lst:
    for j in all_files:
        if j['From'].strip() ==i:
            lst_3.extend(x.strip() for x in j['To'])
            new_relation[i] =lst_3
            lst_3=[]

g = nx.DiGraph()
g.add_nodes_from(new_relation.keys())
for k, v in new_relation.items():
    g.add_edges_from(([(k, t) for t in v]))
    
nx.draw(g, with_labels=True, font_weight='bold')            
