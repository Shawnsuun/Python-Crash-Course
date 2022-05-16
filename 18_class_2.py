#import class from other module
from car import Car

my_new_car=Car('audi','a4','2019')
my_new_car.fill_gas_tank()
print(my_new_car.gas_tank_percentage)

my_new_car.update_odometer(45)
my_new_car.read_odometer()

my_new_car.update_odometer(40)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()

from car import Battery,ElectricCar

my_tesla=ElectricCar('tesla','model s',2021)
my_tesla.carbattery.describe_battery()
my_tesla.carbattery.get_range()
my_tesla.carbattery.upgrade_battery()
my_tesla.carbattery.get_range()

#import whole module
import car

my_beetle=car.Car('volkswagen','beetle',2019)
print(my_beetle.get_description_name())
my_tesla=car.ElectricCar('tesla','roadster',2021)
print(my_tesla.get_description_name())

#import all classes in a module
from car import *

#rename imported class
from car import ElectricCar as EC

my_tesla=EC('tesla','model s',2021)
my_tesla.carbattery.describe_battery()
my_tesla.carbattery.get_range()
my_tesla.carbattery.upgrade_battery()
my_tesla.carbattery.get_range()

#pratice 9-10
from restaurant import Restaurant,IceCreamStand
devon_house_ice_cream=IceCreamStand('Devon House Ice Cream','IceCream & Drinks')
devon_house_ice_cream.show_flavors()

#pratice 9-11
from user import *
shawn=Admin('xiaowen','sun',29,'male')
shawn.privileges.show_privilege()

import user
user.shawn=Admin('xiaowen','sun',29,'male')
user.shawn.privileges.show_privilege()

#pratice 9-12
from user import User
from admin import Privileges_1,Admin_1
shawn=Admin_1('xiaowen','sun',29,'male')
shawn.privileges.show_privilege()

#python standard library
from random import randint
random_number=randint(1,6)
print(random_number)

from random import choice
players=['charles','martina','michael','florence','eli']
first_up=choice(players)
print(first_up)

#pratice 9-14
class Die:
	def __init__(self,sides=6):
		self.sides=sides

	def roll_die(self):
		from random import randint
		print(randint(1,self.sides))

	def multi_roll_dice(self,times):
		self.times=times
		n=0
		while n<self.times:
			self.roll_die()
			n+=1

dice_6=Die()
dice_6.roll_die()
dice_6.multi_roll_dice(10)

dice_10=Die(10)
dice_10.roll_die()
dice_10.multi_roll_dice(10)

dice_20=Die(10)
dice_20.roll_die()
dice_20.multi_roll_dice(10)

#pratice 9-14
from random import choice
pool=[34,77,12,1,8,23,99,38,19,62,'y','w','n','h','q']

prize_number=[]
n=0
while n<4:
	add_number=choice(pool)
	prize_number.append(add_number)
	pool.remove(add_number)
	n=n+1

print("if you get following numbers in your lotto, you will get 500 million dollars!")
print(prize_number)

#pratice 9-15
prize_number=['h', 'n', 8, 38]
my_ticket=[]
n=0
attempt=0
while n<4:
	add_number=choice(pool)
	my_ticket.append(add_number)
	pool.remove(add_number)
	n=n+1
	if n==4:
		attempt+=1
		print(attempt)
		print(my_ticket)

#A Counter is a dict subclass for counting hashable objects.It is an unordered collection where elements are stored as dictionary keys 
#and their counts are stored as dictionary values. 
		
		from collections import Counter
		if dict(Counter(my_ticket))==dict(Counter(prize_number)):
			break

		pool=[34,77,12,1,8,23,99,38,19,62,'y','w','n','h','q']
		my_ticket=[]
		n=0