#list, set, tuple,
# A list is more like an array in other PL  
f_lsit = ['Milkish', 'Milkish', 'Salty']

#use of list comprehension
s_list = [1,2,3,4,5]
s2_list = [ element * 2 for element in s_list ]
print(s2_list)

#converting a list to a list of tuples using enumerate
tupled_list = enumerate(s2_list)
for (index, element) in tupled_list:
    print(element)

#SET doesn't allow duplicated data but mutated
f_set = { 'Milkish', 'Milkish', 'Salty' }


#TUPLE:immutatble are for hard coded list with duplicated entries in a particular order
f_tuple = ( 'Malty', 'Salty', 'Milkish')

#DICTIONARY is mutatble, it just like Javascript objects
f_dic = { 'name' : 'Milk', 'n': 2 }