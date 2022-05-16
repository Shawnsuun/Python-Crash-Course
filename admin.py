#This is a module for pratice 9-12
class Privileges_1:
	def __init__(self):
		self.privileges=['can add post','can delete post','can ban users','can unlock users']

	def show_privilege(self):
		print(self.privileges)

from user import User
class Admin_1(User):
	def __init__(self,first_name,last_name,age,gender):
		super().__init__(first_name,last_name,age,gender)
		self.privileges=Privileges_1()