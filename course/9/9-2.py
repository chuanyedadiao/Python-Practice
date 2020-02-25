class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


res1 = Restaurant("chuanye","Chinese Food")
res1.describe_restaurant()
res1.open_restaurant()
print()
res1 = Restaurant("zhengqing","Indian Food")
res1.describe_restaurant()
res1.open_restaurant()
print()
res1 = Restaurant("xiaozhong","Japanese Food")
res1.describe_restaurant()
res1.open_restaurant()
