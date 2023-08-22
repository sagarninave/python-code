
"""
Example use with filter()
The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is
returned which contains items for which the function evaluats to True.
"""
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)


"""
Example use with map()
The map() function in Python takes 2 argumentd such as function and list.
The function is called with all the items in the list and a new list is
returned which contains items returned by that function for each item.
"""

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)


# Output: [2, 10, 8, 12, 16, 22, 6, 24]



from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
