# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import csv
import json

file=open('csv_file.txt','r')
fr=csv.reader(file)
data=[]
for i in fr:
    data.append(i)
file.close()
a=[]
for i in data:
    b={}
    b['club']=i[0]
    b['country']=i[2]
    b['city']=i[1]
    a.append(b)
file.close()
file=open('json_file.txt','w')
json.dump(a,file)
file.close()