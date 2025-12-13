L = [4, 1, 2, 9, 10, 5, 6, 3, 7, 8]
print("Original list: ", L)
#variable to store the sum of 
#the list
count = 0
#Finding the sum
for i in L:
    count += i
#divide the total elements by
#number of elements
avg = count/len(L)

print("sum -", count)
print("average = ", avg)
#Sorting the elements of the list
L.sort()
#printing the first element
print("Smallest element is:", L[0])
# printing the last element
print ("Largest element is:", L[-1])