#import necassary packages
from abc import ABC, abstractmethod
#create a base class
class animal(ABC):

    #abstract mthod
    #should be implented by all sub-classes
    def move(self):
        pass

#sub classes
class human(animal):

    def move(self):
     print("I can walk and run")

class snake(animal):
    def move (self):
       print("i can crawl")

class dog(animal):
    def move (self):
       print("i can bark")

class lion(animal):
    def move (self):
       print("i can rawr")


#driver code
r = human()
r.move()

k = snake()
k.move
d = dog()
d.move
l = lion()
l.move