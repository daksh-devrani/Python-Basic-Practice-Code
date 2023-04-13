import csv
f=open('csvFile.csv','w',newline='')
fw=csv.writer(f)
while(True):
    name=input('enter name: ')
    age=input('enter age: ')
    data=[name,age]
    fw.writerow(data)
    ch=input('enter yY to continue: ')
    if ch not in 'Yy':
        break
f.close()
f=open('csvFile.csv','r')
fr=csv.reader(f)
for i in fr:
    print(i)