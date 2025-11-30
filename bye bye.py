valid = False
while not valid: #using nested while loop
    try:
        n=int(input("enter a number: "))
        #enter an even number
        while n%2==0:
 

          print("Bye")
        valid = True
    except ValueError:
      print("Invalid")