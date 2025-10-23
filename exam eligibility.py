#Take input of the student if he can attend the exam or not.
medical_cause=input("did you have a medical cause Y or N: ")
#Take input of the attendance.
attent =int(input("enter the attendance of the student: "))

if medical_cause =="Y": #checking the condition 1
    print("you are allowed.")
else:
if atten>= 75: #chexking the condition 2
    print("You are allowed")
else:
    print("You are not allowed")