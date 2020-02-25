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

res = Restaurant("chuanye","Chinese Food")
print("There are total "+str(res.number_served)+" taking dine in the restaurant")

res.number_served = 5
print("There are total "+str(res.number_served)+" taking dine in the restaurant")

res.set_number_served(98)
print("There are total "+str(res.number_served)+" taking dine in the restaurant")

res.increment_number_served(100)
print("There are total "+str(res.number_served)+" taking dine in the restaurant")
