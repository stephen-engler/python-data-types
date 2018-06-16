#immutable 
#once an element is inside at tuple, it can't be reassigned
#(1,2,3)

t = (1,2,3)
mylist = [1,2,3]

print(len(t))

t = ('a', 'a', 'b')

print(t.count('a'))

print(t.index('a'))

# t[0] = 'one' doesn't work

# passing around objects in program and don't want them to change
# data integrity