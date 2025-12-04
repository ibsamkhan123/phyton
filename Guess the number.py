import random  #import module
playing = True #intialise
number = str(random.randint(1,15)) #random inbuilt function
print("I will generate a number from 1 to 15, and you have to guess the number one digit at a time")
print("The game ends when u get 1 hero")
#literate loop while the condition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("the number was", number)
        break
    else:
        print("Your guess isnt quite good, try again!")
