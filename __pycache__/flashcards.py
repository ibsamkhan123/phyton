class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        #we will return a string
        return self.word+'('+self.meaning+')'

flash = []
print("Welcome to flashcard application")

#the following loop will repeat until
#user stops to add flashcards
while(True):
    word = input("Enter the name u want of the flashcard:")
    meaning = input("Enter the meaning of your flashcard:")
    flash.append(flashcards(word, meaning))
    option = int(input("enter 0, if you want to add another flashcard, otherwise add 1:"))

    if(option):
        break
    #printing all the flashcards
    print("\nYour flashcards")
    for i in flash:
        print(">", i)