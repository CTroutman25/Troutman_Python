# Calvin Troutman
# CIS245 Introduction to Programming
# Assignment 8.1 Classes
#
# This program will create a virtual garage that will allow the user to input a car or pickup.
# The program will also allow users to input vehicle attributes of the vehicle selected with the options.


class Vehicle:   # This is the parent class for the virtual garage.
    def __init__(self, make, model):
        self.vehicle_options = {'make': make, 'model': model}

    def setMake(self, make):   # Defining make.
        self.vehicle_options['make'] = make

    def setModel(self, model):   # Defining model.
        self.vehicle_options['model'] = model

    def Features(self):
        self.features = {'features': {'powerWindows': input(f"Does it have power windows? ( y / n )   "),
                'powerDoors': input(f"Does it have power doors? ( y / n )   "),
                'powerLocks': input(f"Does it have power locks? ( y / n )   "),
                'remoteStart': input(f"Does it have remote start? ( y /  n )   "),
                'xm': input(f"Does it have XM Radio? ( y / n )   "),
                'sunroof': input(f"Does it have a sunroof? ( y / n )   "),
                'allwheel': input(f"Does it have all wheel drive? ( y / n )   "),
                'heatedSeats' : input(f"Does it have heated seats? ( y / n )   ")}}

    def displayOptions(self):   # Creating a function to return user input.
        print(f"Make: {self.vehicle_options['make']}")
        print(f"Model: {self.vehicle_options['model']}")


class PickUp(Vehicle):  # This is child class to Vehicles that will make a virtual truck.
    def __init__(self, make, model, bedLength):
        Vehicle.__init__(self, make, model)
        self.vehicle_options = {'make': make, 'model': model, 'bedLength': bedLength}

    def setBedLength(self, bedLength):   # Defining bed length.
        self.vehicle_options['bedLength'] = bedLength

    def displayOptions(self):   # Function to display user input for a truck.
        print(f"Here is the pickup you have created.")
        super().displayOptions()
        print(f"BedLength: {self.vehicle_options['bedLength']}")


class Car(Vehicle):   # A chile class to Vehicle that creates a virtual car.
    def __init__(self, make, model, doors):
        Vehicle.__init__(self, make, model)
        self.vehicle_options = {'make': make, 'model': model, 'doors': doors}

    def setDoors(self, doors):   # Defining doors.
        self.vehicle_options['doors'] = doors

    def displayOptions(self):   # A function that displays user input for virtual car.
        print(f"Here is the car you have created.")
        super().displayOptions()
        print(f"Doors: {self.vehicle_options['doors']}")


print("")
print("Welcome to your virtual garage!")
print("")

garage = []
active = True   # Used to make it easier to get out of while loop

while active:
    VehicleType = int(input("To add a car enter 1, to add a pickup enter 2, to quit enter 3  "))

    if VehicleType == 1:   # Option that creates a car.
        make = (input(f" What is the make?  "))
        model = (input(f" What is the model?  "))
        doors = (input(f" How many doors?  "))
        myCar = Car(make, model, doors)
        garage.append(Car(make, model, doors))
        myCar.displayOptions()
        myCar.Features()

    if VehicleType == 2:   # Options that creates a truck.
        make = (input(f" What is the make?  "))
        model = (input(f" What is the model?  "))
        bedLength = (int(input(f" What is the bed length?  ")))
        myTruck = PickUp(make, model, bedLength)
        garage.append(PickUp(make, model, bedLength))
        myTruck.displayOptions()
        myTruck.Features()


    if VehicleType == 3:   # Allows user to quit adding virtual vehicles.
        active = False
