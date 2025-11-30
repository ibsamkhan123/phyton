try:
    num1, num2 = eval(input("Enter 2 numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is: ", result)
#using multiple except block for different type of error

except ZeroDivisionError:
    print("Division with 0 is an error!!!")

except SyntaxError:
    print("Comma is missing! Enter numbers with comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No Exeptions")

finally:
    print("this will execute no matter what!!!")