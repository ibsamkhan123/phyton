#take marks as input from user
print("Enter marks obtained in 4 subjects:")
math =int(input("maths :"))
english =int(input("english :"))
history =int(input("history :"))
french =int(input("french :"))
#Lets calculate the precentage of marks!
sum =math+english+history+french
print("sum of math,english,history and french")
perc=(sum/400)*100

print(end="Percentage mark")
print(perc)