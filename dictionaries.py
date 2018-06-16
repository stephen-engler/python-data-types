#unordered mappings to store objects
#key value pair
#{'key1': 'value1', 'key2': 'value2'}
#dic can't be sorted 

my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict['key1'])

prices_lookup = {'apples': 2.99, 'oranges': 1.99, 'milk': 4.99}

print(prices_lookup['apples'])

#can hold lists or other dict

d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)

d['k1'] = 'new value'
print(d)

print(d.keys())
print(d.values())
print(d.items())