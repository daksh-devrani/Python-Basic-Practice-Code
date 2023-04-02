a=[1,2,3,4,5,6,7,8,9]
num=int(input('Enter number to search: '))
b=0
for i in range(len(a)):
    if a[i]==num:
        print('number at',i,'index')
        b+=1
if b==0:
    print('number not in list')