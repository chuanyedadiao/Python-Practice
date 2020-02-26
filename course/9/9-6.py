class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")
        
    def set_number_served(self,number_served):
        self.number_served = number_served
    def increment_number_served(self,number_increase):
        self.number_served += number_increase

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["Strawberry","BlueBerry","Milk"]
    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor,end=" ")


icecream = IceCreamStand("chuanye","ice cream")
icecream.describe_restaurant()
icecream.describe_flavors()
