class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.serve_number=0

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} is a restaurant of {self.cuisine_type.title()} cuisine.")

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is now open!")

	def number_served(self):
		print(f"Served Number:{self.serve_number}")

	def set_number_served(self,number_new_served):
		self.serve_number=number_new_served

	def increment_number_served(self,number_increment):
		self.serve_number+=number_increment

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['strawberry','lemon','chocolate','coconut','Rum']

	def show_flavors(self):
		print(f"Welcome to {self.restaurant_name.title()}!")
		print("You can select from these flavors!")
		for flavor in self.flavors:
			print(f"\t{flavor.title()}")