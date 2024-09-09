''''
You can copy this code into your own file or clone this project (we'll learn how to do this soon) to run it and play around with. 
You can run the code and see what happens. You can change the values or run different functions to continue learning about these data structures.

Ask your questions in #study-hall!
'''

# Lists

# How can we create a list?

list_literal = []

list_constructor = list()

# How do we add elements to a list?
list_literal.append(5)
list_literal.append(10)
list_literal.append(15)
list_literal.append(20)

print(f"{list_literal=}")

# How do we remove elements from a list?
# Documentation you can look at: https://docs.python.org/3/tutorial/datastructures.html

list_literal.pop()
print("Popped one element from end of list", list_literal)

# What if you want to do something with the removed item like print it?

popped_element = list_literal.pop(1)
print(f"{popped_element=}")

# Dictionaries

# How do we create dictionaries? 
# Only immutables can be used as keys

student_dict = {"name": "Claire", "city": "Seattle"}
drink_prices = dict(mango = 2.5, orange = 3)

print(student_dict)
print(drink_prices)

# Some operations we can perform on dictionaries

a_first = {}
a_first["a"] = 1
a_first["b"] = 2

b_first = {}
b_first["b"] = 2
b_first["a"] = 1

print(a_first)
print(b_first)
print("a_first compared to b_first is", a_first == b_first)

# Set
'''
Unique and immutable elements.
Elements are unordered.
'''

# How can we create a set?

set_literal = {1, 2, 3, 4, 5}
# What happens when we uncomment line 64 and execute the code?
# set_constructor = set(3, 4) 
set_constructor = set()

# How do we add an element to a set?

set_literal.add(6)

set_constructor.add(3)
set_constructor.add(4)

# What are some ways we can remove elements from a set?

set_literal.remove(1)
print(f"{set_literal=}")
print(f"{set_constructor=}")

# What's the difference between remove and discard?
set_literal.discard(100)

# Uncomment line 85 and execute the code to see what happens
# set_literal.remove(100) 

# What are some other things we can do with a set?

# Union: combines the sets into a new set that includes all of the elements of the original sets. 
# Any overlapping elements are included only once in the result set.
result_set_1 = set_literal.union(set_constructor) 

result_set_2 = set_literal | set_constructor

print(f"{result_set_1=}")
print(f"{result_set_2=}")

# Intersection: a new set composed of all of the elements that were present in both sets

result_set_3 = set_literal.intersection(set_constructor) 

result_set_4 = set_literal & set_constructor 

print(f"{result_set_3=}")
print(f"{result_set_4=}")

# Difference: new set composed of all of the elements of the first set except for any elements that overlap with the second set

result_set_5 = set_literal.difference(set_constructor) 

result_set_6 = set_literal - set_constructor 

print(f"{result_set_5=}")
print(f"{result_set_6=}")


# Tuples
'''
A tuple is an ordered, immutable collection of elements. 
The length and data type of each element in a tuple never changes. 
This means that elements cannot be added, replaced, or removed.
Tuples can store any data type including mutable data types like lists and dictionaries.
'''

# How can we create a tuple?

tuple_constructor = tuple([1, 2, 3, 3])
tuple_literal = (1, 2, 3, 3)
tuple_san_parens = 1, 2, 3, 3

# How can we access elements from a tuple?
tuple_constructor[0]
tuple_literal[-1]

names_list = ["Ravi", "Hailey"]
tuple_with_list = (names_list,)

print(tuple_with_list)

names_list.append("Piper")
print("What does a tuple look like after an element is added to the list it holds?", tuple_with_list)

# Uncomment line 150 to see what happens when we try to replace names_list in the tuple
emails_list = ["coder4lyfe@gmail.com", "absent@adadevelopersacademy.org"]
# tuple_with_list[0] = emails_list