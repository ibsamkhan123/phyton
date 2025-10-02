#input a word
text=str(input("Enter a string:  "))
#Reverse string
#using step value -1 to iterate in reverse
revText=text[::-1]
text= revText
print("Reverse of given string is:")
print(text)