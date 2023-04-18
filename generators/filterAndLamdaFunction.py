def starts_with_D(f):
    return f.startswith('D')
friends=['Daksh','Divyansh','Jagrath']
s=filter(starts_with_D,friends)
print(list(s))
s=filter(lambda x: x.startswith('D'),friends)
print(list(s))
print(list(f for f in friends if f.startswith('D')))