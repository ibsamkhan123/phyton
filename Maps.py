#Add 2 lists using map and lambda
numbers1 = [9,12,303]
numbers2 = [8,16,404] 
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of 2 lists")
print(list(result))


#using map
nums = [3, 9, 12, 15, 18]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)
