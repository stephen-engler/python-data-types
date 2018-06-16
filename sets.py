#unordered collections of uniqe elements
myset = set()

myset.add(1)
# looks like a dict with curly braces but no key value pair
print(myset)
myset.add(2)
#won't add because already in
myset.add(1)

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4]
print(set(mylist))