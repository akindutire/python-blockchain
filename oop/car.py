from vehicle import Vehicle

#Inheritance

class Car(Vehicle):

    #Private instance is denoted with __ preceeding such property
    __private_intance = 34

    def __init__(self):
        self.top_speed = 45

    def drive(self):
        print("Drive at {}".format(self.top_speed))
    
    def get_private_instance(self):
        return self.__private_intance

c = Car()

print(c.__str__)
 
# c.drive()

"""
    Note
    1.   array_merge is php is simila to array.extend(array) in python

"""