#zip elements of 2 lists
s1 = [3,1,2]
s2 = ['c','a','b']
s3 = list(zip(s1, s2))
print(s3,"\n")


#Zip elements of 2 lists
#Print elements one by one, but elements of the 2nd list will be in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip (list1, list2[::-1]):
    print(x, y)


#Zip into dictionary
stocks = ['reliance','infosys','tcs']
prices = [2175 , 1125 , 2750]
new_dict = {stocks:prices for stocks,
                      prices in zip (stocks, prices)}
print('\n{}'.format (new_dict))