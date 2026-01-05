#create class
class parrot:

    #class attribute
    species = "bird"
    #instance attribue
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the parrot class
wooo = parrot("wooo", 19)
taqqi = parrot("taqqi", 15)

#access the class attributes
print("wooo is a {}".format(wooo.species))
print("taqqi is a {}".format(taqqi.species))
#access the instance attribute
print("{} is {} years old".format(wooo.name, wooo.age))
print("{} is {} years old".format(taqqi.name, taqqi.age))