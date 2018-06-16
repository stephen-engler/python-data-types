a = 10 
print(type(a))

my_name = "Stephen"

# reverse index 
print(my_name[-1])

# slicing [start : stop : step ]
# stop index upto but not include 
#  step is size of jump to take

# escape characters \n \t 
print('hello \n world')

len('hello')

#slicing
mysting = 'hello world'
print(mysting[-2])
mysting = 'abcdefghifk'
print(mysting[2:])
print(mysting[:3])
print('middle sting ', mysting[3:6])
print('step stuff ', mysting[::2])
# reverse sting
mysting[::-1]

#properties and methods
#strings are immutable
#sting concatination
name = 'Sam'
new_name = 'P' + name[1:]
print(new_name)

#string methods
x = 'hello world'
print(x.upper())
print(x.split())

#print formating string interpolation
#.format()
print('this is a {}, how cool is {}'.format('string', 'this'))
print('the {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#float formating
result = 100/77
print('the result was {r:1.3f}'.format(r=result))

#f strings
name = 'stephen'
print(f'hello, my name is {name}')