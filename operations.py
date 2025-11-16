def add(I, K):
    #This function is used for adding 2 numbers
 return I + K
def substract(I, K):
    #This function is used for substracting 2 numbers
 return I - K
def multiply(I, K):
    #This function is used for multiplying 2 numbers
 return I * K
def divide(I, K):
    #This function is used for dividing 2 numbers
 return I / K
#Now will take inputs from user
print("Please select the operation.")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide")
choice = input("Please enter choice(a/ b/ c/ d/):")

num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter the second number: "))


if choice == 'a':
 print(num_1,"+",num_2,"=", add(num_1, num_2))
elif choice == 'b':
 print(num_1,"-",num_2,"=", substract(num_1, num_2))
elif choice == 'c':
 print(num_1,"*",num_2,"=", multiply(num_1, num_2))
elif choice == 'a':
 print(num_1,"/",num_2,"=", divide(num_1, num_2))
else:
 print("This is an invalid input")
