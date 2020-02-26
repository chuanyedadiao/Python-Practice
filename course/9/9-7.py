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

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print("Admin's privileges:")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Yushun","Xu",21)
admin.describe_user()
admin.show_privileges()
