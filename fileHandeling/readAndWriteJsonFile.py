import json
file=open('JSON.txt','r')
data=json.load(file)
print(data['friends'][0])
file.close()
file=open('JSON.txt','w')
json.dump(data,file)
file.close()