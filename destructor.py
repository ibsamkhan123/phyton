#create class
class employee:
    #intializing
    def __innit__(self):
        print("Employee created")
        #Calling destructor
    def __del__(self):
            print("destructor called")
def Create_obj():
    print('Maing Object...')
    obj = employee()
    print('function end...')
    del obj
        
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')