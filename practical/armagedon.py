num=int(input('enter number: '))
num2=0
for i in str(num):
    num2+=int(i)**3
if num2==num:
    print('yes')
else:
    print('no')
