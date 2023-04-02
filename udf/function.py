def no_Argument_no_Return():
    a=100
    b=200
    c=a+b
    print(c)

def no_Argument_with_Return():
    a=100
    b=200
    c=a+b
    return c

def argumrnt_no_Return(a,b):
    c=a+b
    print(c)

def argument_with_Return(a,b):
    c=a+b
    return c


no_Argument_no_Return()
value=no_Argument_with_Return()
print(value)
value=argumrnt_no_Return(100,200)
value=argument_with_Return(100,200)
print(value)