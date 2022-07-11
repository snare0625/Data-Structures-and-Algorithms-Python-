myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
newDict = {}.fromkeys([1, 2, 3], 0)
#print(newDict)
#print(myDict.get('age', 27))
print(myDict.setdefault('name1', 'added'))
del1 = {'a':1, 'b': 2, 'c':3}
myDict.update(del1)
print(myDict)
