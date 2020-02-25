class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name = last_name
        self.age=age

    def describe_user(self):
        print("FirstName:\t"+self.first_name)
        print("LastName:\t"+self.last_name)
        print("Age:\t\t"+str(self.age))

    def greet_user(self):
        print("Ohiyo Hi "+self.first_name)

person1 = User("Yu Shun","Xu",21)
person1.describe_user()
person1.greet_user()
print()

person1 = User("Xiang","Zhou",20)
person1.describe_user()
person1.greet_user()
print()

person1 = User("Yi Yue","Zhong",21)
person1.describe_user()
person1.greet_user()
