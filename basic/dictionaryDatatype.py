dictionary={'name':'Daksh','age':17}
print(dictionary)
dictionary['school']='alma mater'
print(dictionary)
print(dictionary.get('name'))
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
print(dictionary.pop('school'))
dict2=dictionary.copy()
print(dict2)
dictionary.setdefault('school','Alma mater')
print(dictionary)