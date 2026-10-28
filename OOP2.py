class car:
    def __init__(self, brand, model, colour, transmission):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.transmission = transmission
brand = input("Enter the brand of the car: ")
model = input("Enter the model of the car: ")
colour = input("Enter the colour of the car: ")
transmission = input("Enter the transmission of the car: ")
car1 = car(brand=brand, model=model, colour=colour, transmission=transmission)
print("The car is a", car1.colour, car1.brand, car1.model, "with", car1.transmission, "transmission.")