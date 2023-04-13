def saveToFile(content,filename):
    f=open(filename,'w')
    f.write(content)
    f.close()

def readFile(filename):
    f=open(filename,'r')
    data=f.read()
    print(data)
