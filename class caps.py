# create class
class IOString():
    #constructor to set default value
    def __init__(self):
        self.strl = ""
        #function ot get input from user
    def get_String(self):
            self.strl = input("enter String:")
            #function to get sting in upper case
    def print_String(self):
                print("Result is: ",self.strl.upper())

#Object creation
strl = IOString()
#Call functions
strl.get_String()
strl.print_String()