#Create a tuple with different data types
tuplex = ("tuple",False, 3.2, 1)
print(tuplex)
#create a tuple
tuplex = (2, 4, 8, 6, 1, 3)
print(tuplex)
#tuples are immutable, so you cannot add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#counts the number of occurrences of item 50 from a tuple
tuplel = (60, 70, 10, 50, 50)
print(tuplel.count(50))
#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 1, 6)
#used tuple [start:stop] the start index is inclusive and the stop index 
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beginning of the tuple 
_slice = tuplex [:6]
print(_slice)