#Taking total amount from user
Amount=int(input("Please enter amount for withdraw :"))
#Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100 rupees" ,note_1)
print("Notes of 50 rupees" ,note_2)
print("Notes of 10 rupees" ,note_3)