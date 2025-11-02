#Take input of a world
string = input("Enter your own word : ")
#take input of a character
char = input("Enter your own Character : ")
o = 0
count = 0
#loop will find the occurence of character
while(o < len(string)): #string operation
    if(string[o] == char):#condition 1
        count = count+1
    o = o+1
#display the result
print("The total number of times ", char, "has Occured =", count)    

