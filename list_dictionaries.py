#lists ordered sequence 
#[] 

my_list = [1,2,3]
print(len(my_list))

this_list = ['one', 'two', 'three']
print(this_list[0])
print(this_list[1:])

another_list = ['four', 'five']

print( this_list + another_list)

#lists are mutable
this_list[0] = 'ONE'
print(this_list)
#affect in place
this_list.append('four')
print(this_list)

#pop removes from end
#pop also returns what was removed
this_list.pop()
print(this_list)
this_list.pop(0)
print(this_list)

#sort and reverse
abc_list = ['a', 'g', 'z', 'e', 't']
#doesn't return anything sorts in place 
abc_list.sort()
print(abc_list)

#reverse
#again doesn't return anything sort in place
abc_list.reverse()
print(abc_list)