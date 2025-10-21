# Come out with class
# under class, come out with Accessor Method and if changes are needed, come out with Mutator Method
# if calculations are needed, come out with an Accessor 
 
class PetrolPurchase:
    def __init__(self, station_location, quantities, type_of_petrol, price_of_petrol, discount_percentage):
        self.station_location = station_location
        self.quantities = quantities
        self.type_of_petrol = type_of_petrol
        self.price_of_petrol = price_of_petrol
        self.discount_percentage = discount_percentage

    def get_station_location(self): # Accessor Method, It is used to retrieve or access the value of 
                                    # the station_location attribute from an instance of 
                                    # the PetrolPurchase class. When you call this method, 
                                    # it returns the current value of the station_location.
        return self.station_location 
    
    def set_station_location(self, station_location): # Mutator Method, It is used to modify or 
                                                      # update the value of the station_location attribute 
                                                      # for an instance of the PetrolPurchase class. When you call this method with a new value, it sets the station_location to that value.
        self.station_location = station_location

    def get_quantities(self):
        return self.quantities

    def set_quantities(self, quantities):
        self.quantities = quantities 

    def get_type_of_petrol(self):
        return self.type_of_petrol
    
    def set_type_of_petrol(self, type_of_petrol):
        self.type_of_petrol = type_of_petrol

    def get_price_of_petrol(self):
        return self.price_of_petrol
    
    def set_price_of_petrol(self, price_of_petrol):
        self.price_of_petrol = price_of_petrol

    def get_discount_percentage(self):
        return self.discount_percentage
    
    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def total_cost(self):
        return self.quantities * self.price_of_petrol
    
    def discount(self):
        return self.total_cost() * (self.discount_percentage / 100)
    
    def final_price(self):
        return self.total_cost() - self.discount()
    
    def __str__(self, title="Summary of purchase"): # __str__ is just helps with print in the format you want
                                                    # used for more design friendly and readibility
        return (
            f"\n{title}\n"
            f"\tStation: {self.station_location}\n" # it is not self.get_station_location 
                                                    # because you are not suppose to use a getter in a getter

                                                    # or you can type self.get_station_location() 
                                                    # because you are called the function to help you do the job
            f"\tQuantities: {self.quantities:.2f}\n"
            f"\tType of petrol: {self.type_of_petrol}\n"
            f"\tUnit price: {self.price_of_petrol:.2f}\n"
            f"\tDiscount: {self.discount_percentage:.2f}%\n"
            f"\tTotal cost: {self.total_cost():.2f}\n"
            f"\tTotal discount: ({self.discount_percentage:.2f}%): ${self.discount():.2f}\n"
            f"\tFinal payment: ${self.final_price():.2f}"
        )
    
    def __repr__(self): # works like __str__, helps with print in the format you want
                        # used for offical and development friendly
        return (
            f'PetrolPurchase("{self.station_location}", {self.quantities}, "{self.type_of_petrol}", '
            f'{self.price_of_petrol}, {self.discount_percentage})'
        )

station = input("Enter the station: ")
quantity = float(input("Enter quantities in litres: "))
petrol_type = input("Enter type of petrol: ")
price_per_litre = float(input("Enter price of petrol: "))
discount = float(input("Enter discount: "))

purchase = PetrolPurchase(station, quantity, petrol_type, price_per_litre, discount) # creating purchase object


print(str(purchase)) # printing the object which will use __str__ method
                          # used for more design friendly and readibility

additional_quantity = float(input("\nAdditional quantity: "))
purchase.set_quantities(purchase.get_quantities() + additional_quantity) # use the mutator to change the value

print(purchase.__str__(title="Final Summary of purchase")) #print the object again which will use __str__method

print("\nThe object was constructed according to:")
print(repr(purchase)) # printing the object which will use __repr__ method
                           # used for more offcial and development friendly

input("\nPress Enter to terminate")