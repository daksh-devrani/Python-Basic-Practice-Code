def bubbleSort(list1):
    n=len(list1)
    swaped=False
    for i in range(n-1):
        for j in range(n-i-1):
            if list1[j]>list1[j+1]:
                swaped=True
                list1[j],list1[j+1]=list1[j+1],list1[j]
    if not swaped:
        return
a=[1,4,2,3,6,8]
bubbleSort(a)
print(a)
