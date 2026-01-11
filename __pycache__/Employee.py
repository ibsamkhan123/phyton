#parent class
class person( object ):

                #__innit__ is known as a constructor
                def __init__(self, name, idnumber):
                        self.name = name
                        self.idnumber = idnumber
                def display(self):
                         print(self.name)
                         print(self.idnumber)

 #child class
class employee( person ):
                def __init__(self, name, idnumber, salary, post):
                        self.salary = salary
                        self.post = post
                        #invoking the __innit__ of the parent class
                        person.__init__(self, name, idnumber)

#creation of an object variable or an instance
a = employee ('Ibsam', 67611293, 200000, "Intern") 
#Calling a function of the class person usint its instance
a.display()