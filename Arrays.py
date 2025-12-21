import array as arr
#create an erray
array_num = arr.array('i', [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])
print("Original array:"+str(array_num))

#current numbers of occurences
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))

#reverse the array
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))