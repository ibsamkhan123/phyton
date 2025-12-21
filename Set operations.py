#Different types of sets in python 
#set of integers
my_set = {1, 2, 3}
print(my_set)

#set of mixed datatypes
my_set = {1.0,"Hello", (1, 2, 3)}
print(my_set)

#set cannot have duplicates
my_set = {1, 2, 3, 4, 4, 3, 2, 1}
print(my_set)
# we can make set of a list
my_set = set([1, 2, 3, 2])
print(my_set,"\n")

#remove a number from a set
num_set = set([0, 1, 3, 4, 5])
print("Original set: ")
print(num_set)
num_set.pop()
print("After removing te first element for the said set:")
print(num_set,"\n")