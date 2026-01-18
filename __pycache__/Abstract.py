from abc import ABC, abstractmethod
#create bass class
class Absclass(ABC):
    #function to print a value
    def print(self,x):
        print("Passed value: ", x)

    #Abstract method
    @abstractmethod
    def task(self):
        print("we are inside Absclass task")

#create sub class
class test_class(Absclass):   
     def task(self):
            print("we are inside text_class task")

#obj of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
