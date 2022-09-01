# Datatypes

# Data types are the classification or categorization of data items. 
# It represents the kind of value that tells what operations can be performed on a particular data. 

# Numeric
# Boolean
# Sequence types => Strings, Lists, Tuples
# Dictionary
# Set

# Numbers
price = 99.07
age = 32
result = 2 + 3j
# Checking data type
print(type(result))
# TODO - Check the datatype for age and price

# Boolean
is_hungry = True
is_weekend = False
# TODO - Check the datatype for is_hungry and is_weekend

# Strings
subject = "Python programming language"
name = 'John Bull'
# TODO - Check the datatype for subject and name

# Accessing elements of string
print(subject[0])
print(subject[1])
print(subject[2])
print(subject[2:6])
print(subject[2:10:2])
print(subject[2:10:-1])
print(subject[::])
print(subject[::-1])

# Lists
fruits = ['apple','orange', 'paw-paw', 'banana']
even_numbers = [2, 4, 6, 8]
# TODO - Display even_numbers and fruits

# TODO - Create a list of your favourite movie shows

# Accessing elements of lists
print(fruits[0])
print(fruits[2])
print(fruits[2:4])
print(fruits[::-1])

# Tuples
# Just like list, tuple is also an ordered collection of Python objects. 
# tuples are immutable i.e. tuples cannot be modified after it is created. 
my_tuple = (2, 3, 4,5,6)
tuple_from_list = tuple(fruits)

# TODO - diplay the tuples
# TODO - What datatype is my_tuple and tuple_from_list

# Assessing elements of tuple
print(my_tuple[2])

# dictionary
empty_dict = dict()
person = {
    "name": "Samuel",
    "age": 34,
    "is_hungry": False
}
print(person)
print(person['name'])
print(person['age'])
print(person['is_hungry'])

# Add and update data to dictionary
person["gender"] = 'Male'
person['is_hungry'] = True
print(person)

# Set
# an unordered collection of data type that is iterable, mutable and has no duplicate elements. 
# The order of elements in a set is undefined though it may consist of various elements
set1 = set()
set_from_list = set(fruits)
num_set = {2, 4, 5, 2, 3, 4, 10, 2.0, 3}
print(set_from_list)
# TODO - Display the num_set

# Readings
# https://www.geeksforgeeks.org/python-data-types/