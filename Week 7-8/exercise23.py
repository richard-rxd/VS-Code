set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

frozenset({3, 4, 3, 2, 2, 5})
try: 
    frozenset.add(8)
except AttributeError:
    print("AttributeError")

print(set1 - set2)
print(set1.difference(set2))