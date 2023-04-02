a=[1,2,3,4,5,6,7,8,9]
a.sort()
low=0
high=len(a)
num=int(input('enter number to find: '))
b=0
if num in a:
    while b==0:
        mid=(high+low)//2
        if a[mid]==num:
            print('num at',mid,'index')
            b=1
        elif a[mid]<num:
            low=mid-1
        elif a[mid]>num:
            high=mid+1

