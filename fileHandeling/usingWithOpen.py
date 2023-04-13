import csv
import json

with open('csv_file.txt','r') as file, open ('json_file.txt','w') as file2:
    fr=csv.reader(file)
    data=[]
    for i in fr:
        data.append(i)
    a=[]
    for i in data:
        b={}
        b['club']=i[0]
        b['country']=i[2]
        b['city']=i[1]
        a.append(b)
    json.dump(a,file2)
