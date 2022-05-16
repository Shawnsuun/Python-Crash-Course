#This is a module for pratice 9-11 and 9-12
class User:
	def __init__(self,first_name,last_name,age,gender):
		self.first_name=first_name
		self.last_name=last_name
		self.gender=gender
		self.age=age
		self.login_attempts=0

	def describe_user(self):
		print(f"\n{self.first_name.title()} {self.last_name.title()} is a {self.gender} user who is {self.age} years old.")

	def greet_user(self):
		if self.gender=='male':
			print(f"Hello, Mr {self.last_name.title()}.")
		else:
			print(f"Hello, Ms {self.last_name.title()}.")

	def increment_login_attempts(self):
		self.login_attempts+=1

	def reset_login_attempts(self):
		self.login_attempts=0

	def count_attempts(self):
		print(f"Login attempt times:{self.login_attempts}")

class Privileges:
	def __init__(self):
		self.privileges=['can add post','can delete post','can ban users']

	def show_privilege(self):
		print(self.privileges)

class Admin(User):
	def __init__(self,first_name,last_name,age,gender):
		super().__init__(first_name,last_name,age,gender)
		self.privileges=Privileges()
