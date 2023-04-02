value=eval(input('enter value: '))
if type(value) is int:
    b=value
    c=0
    while b>0:
        d=b%10
        c=(c*10)+d
        b//=10
    if c==value:
        print('number is a palindrome')
    else:
        print('not a palindrome')
elif type(value) is str:
    b=value[::-1].lower()
    if b==value.lower():
        print('it is a palindrome')
    else:
        print('not a palindrome')


