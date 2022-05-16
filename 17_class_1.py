#create class Dog
class Dog:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")
 
#create example based on class
my_dog=Dog('Willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog=Dog('Lucy',3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

#pratice 9-1
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} is a restaurant of {self.cuisine_type.title()} cuisine.")

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is now open!")

restaurant_1=Restaurant('Bingsheng','cantonese')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

#pratice 9-2
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is a restaurant of {self.cuisine_type.title()} cuisine.")

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is now open!")

restaurant_1=Restaurant('Bingsheng','cantonese')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2=Restaurant('papaya','italian')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3=Restaurant('shake shack','american')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()

#pracice 9-3
class User:
	def __init__(self,first_name,last_name,age,gender):
		self.first_name=first_name
		self.last_name=last_name
		self.gender=gender
		self.age=age

	def describe_user(self):
		print(f"\n{self.first_name.title()} {self.last_name.title()} is a {self.gender} user who is {self.age} years old.")

	def greet_user(self):
		if self.gender=='male':
			print(f"Hello, Mr {self.last_name.title()}.")
		else:
			print(f"Hello, Ms {self.last_name.title()}.")

user_1=User('Mary','Jane','24','female')
user_1.describe_user()
user_1.greet_user()

user_1=User('Jack','Sparrow','30','male')
user_1.describe_user()
user_1.greet_user()

#car class
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year

	def get_description_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car=Car('audi','a4','2019')
print(my_new_car.get_description_name())

#defult value for property
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0

	def get_description_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car=Car('audi','a4','2019')
print(my_new_car.get_description_name())
my_new_car.read_odometer()

#revise property value
my_new_car.odometer_reading=23
my_new_car.read_odometer()

#revise property value by method
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0

	def get_description_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You cannot roll back an odometer!")

	def increment_odometer(self,miles):
		if miles>=0:	
			self.odometer_reading+=miles
		else:
			print("You cannot roll back an odometer!")

my_new_car=Car('audi','a4','2019')
my_new_car.update_odometer(45)
my_new_car.read_odometer()
my_new_car.update_odometer(40)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()

#pratice 9-4
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

restaurant_1=Restaurant('Bingsheng','cantonese')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.number_served()
restaurant_1.set_number_served(10)
restaurant_1.number_served()
restaurant_1.increment_number_served(500)
restaurant_1.number_served()

#pratice 9-5
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

user_1=User('Mary','Jane','24','female')
user_1.describe_user()
user_1.greet_user()

user_2=User('Jack','Sparrow','30','male')
user_2.describe_user()
user_2.greet_user()

user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.count_attempts()

user_2.reset_login_attempts()
user_2.count_attempts()

#inherit from class
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
		self.gas_tank_percentage=0

	def get_description_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You cannot roll back an odometer!")

	def increment_odometer(self,miles):
		if miles>=0:	
			self.odometer_reading+=miles
		else:
			print("You cannot roll back an odometer!")

	def fill_gas_tank(self):
		self.gas_tank_percentage=100

my_new_car=Car('audi','a4','2019')
my_new_car.fill_gas_tank()
print(my_new_car.gas_tank_percentage)

#rewrite method of superclass
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size=75

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-KWh battery.")

	def fill_gas_tank(self):
		print("This car doesn't need a gas tank.")

my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_description_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

#seperate a small class
class Battery:
	def __init__(self,battery_size=75):
		self.battery_size=battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-KWh battery.")

	def get_range(self):
		if self.battery_size==75:
			range=260
		elif self.battery_size==100:
			range=315
		print(f"This car can go about {range} miles on a full charge.")	

#use class battery in class electriccar
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.carbattery=Battery()

my_tesla=ElectricCar('tesla','model s',2019)
my_tesla.carbattery.describe_battery()
my_tesla.carbattery.get_range()

#pratice 9-6
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['strawberry','lemon','chocolate','coconut','Rum']

	def show_flavors(self):
		print(f"Welcome to {self.restaurant_name.title()}!")
		print("You can select from these flavors!")
		for flavor in self.flavors:
			print(f"\t{flavor.title()}")

devon_house_ice_cream=IceCreamStand('Devon House Ice Cream','IceCream & Drinks')
devon_house_ice_cream.show_flavors()

#pratice 9-7
class Admin(User):
	def __init__(self,first_name,last_name,age,gender):
		super().__init__(first_name,last_name,age,gender)
		self.privileges=['can add post','can delete post','can ban users']

	def show_privilege(self):
		print(self.privileges)

shawn=Admin('xiaowen','sun',29,'male')
shawn.describe_user()
shawn.greet_user()
shawn.show_privilege()

#pratice 9-8
class Privileges:
	def __init__(self):
		self.privileges=['can add post','can delete post','can ban users']

	def show_privilege(self):
		print(self.privileges)

class Admin(User):
	def __init__(self,first_name,last_name,age,gender):
		super().__init__(first_name,last_name,age,gender)
		self.privileges=Privileges()

shawn=Admin('xiaowen','sun',29,'male')
shawn.privileges.show_privilege()

#pratice 9-9
class Battery:
	def __init__(self,battery_size=75):
		self.battery_size=battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-KWh battery.")

	def get_range(self):
		if self.battery_size==75:
			range=260
		elif self.battery_size==100:
			range=315
		print(f"This car can go about {range} miles on a full charge.")	

	def upgrade_battery(self):
		if self.battery_size<=100:
			self.battery_size=100

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.carbattery=Battery()

my_tesla=ElectricCar('tesla','model s',2019)
my_tesla.carbattery.describe_battery()
my_tesla.carbattery.get_range()
my_tesla.carbattery.upgrade_battery()
my_tesla.carbattery.get_range()