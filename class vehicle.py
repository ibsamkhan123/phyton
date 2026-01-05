#create class
class vehicle:

    #create init method
   def __init__(self, max_speed, mileage):
              #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = vehicle(240, 18)

#access the variables inside init method
print("Model max speed:", modelX.max_speed)
print("Model Mileage",modelX.mileage)