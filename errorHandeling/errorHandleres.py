i=0
try:
    while(True):
        i+=1
        if i==5:
            raise NotImplementedError()
except NotImplementedError:
    print('yes')