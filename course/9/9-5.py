class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name = last_name
        self.age=age
        self.login_attempts = 0

    def describe_user(self):
        print("FirstName:\t"+self.first_name)
        print("LastName:\t"+self.last_name)
        print("Age:\t\t"+str(self.age))

    def greet_user(self):
        print("Ohiyo Hi "+self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Zheng Qing","Chen",46)

for i in range(20):
    user.increment_login_attempts()
    print("This user's login_attempts is "+ str(user.login_attempts))
    
user.reset_login_attempts()
print("After reset,this user's login_attempts is "+ str(user.login_attempts))
