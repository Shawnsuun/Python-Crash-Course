#for loop each list element
magicians=['alice','david','carolina']
for magician in magicians:
 print(magician)

magicians=['alice','david','carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everybody. That was a great magic show!")

#forget intented block
magicians=['alice','david','carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
#next line won't loop
print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everybody. That was a great magic show!")

#pratice4-1
pizzas=['pepperoni','hawaii','classic']
for pizza in pizzas:
 print(f"I love {pizza} pizza.")
print("I really love pizza!")

#pratice4-2
pets=['cats','dogs','goldfish']
for pet in pets:
 print(f"A {pet} would make a great pet.")
print("Any of these animals would make a great pet!")

#print number 1~4
for value in range(1,5):
 print(value)

#print number 0~4
for value in range(5):
 print(value)

numbers=list(range(1,6))
print(numbers)

#even numbers with step=2
even_numbers=list(range(2,11,2))
print(even_numbers)

#list of squire from 1~10
squires=[]
for value in range(1,11):
 squire=value**2
 squires.append(squire)
print(squires)

#omit "squire"
squires=[]
for value in range(1,11):
 squires.append(value**2)
print(squires)

digits=[]
for value in range(10):
 digits.append(value)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

squires=[value**2 for value in range(1,11)]
print(squires)

#pratice 4-3
numbers=[value for value in range(1,21)]
print(numbers)

#pratice 4-4
for value in range(1,101):
 print(value)

#pratice 4-5
list=[]
for value in range(1,1000001):
 list.append(value)
print(min(list))
print(max(list))
print(sum(list))

#pratice 4-6
digits=[]
for value in range(1,21,2):
 digits.append(value)
 print(value)
print(digits)

#pratice 4-7
digits=[]
for value in range(1,11):
 digits.append(3*value)
 print(3*value)
print(digits)

#pratice 4-8
digits=[]
for value in range(1,11):
 digits.append(value**3)
 print(value**3)
print(digits)

#pratice 4-9
digits=[value**3 for value in range(1,11)]
print(digits)

#slice
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[4:])
print(players[-3:])
print(players[-3::2])

#for loop each slice element
players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())

#create a copy of a list,add element separatly
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#This do not work,because the two lists point to the same list
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#pratice 4-10
players=['charles','martina','michael','florence','eli']
selected_players=players[:3]
print("The first three players in this list are:")
for player in selected_players:
 print(player.title())

players=['charles','martina','michael','florence','eli']
selected_players=players[1:4]
print("The three players in the middle of the list are:")
for player in selected_players:
 print(player.title())

players=['charles','martina','michael','florence','eli']
selected_players=players[2:]
print("The last three players in this list are:")
for player in selected_players:
 print(player.title())

#pratice 4-11
pizzas=['pepperoni','hawaii','classic']
friend_pizzas=pizzas[:]
pizzas.append('chicken')
friend_pizzas.append('durian')
print("My favorite pizzas are:")
print(pizzas)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas[:]:
 print(pizza)

#tuple
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

dimensions=(200,50)
for dimension in dimensions:
 print(dimension)

#change tuple element
dimensions=(200,50)
print("original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions=(400,100)
print("\nmodified dimensions:")
for dimension in dimensions:
 print(dimension)

#pratice 4-11
foods=('burger','chips','cake','salad','pizza')
for food in foods:
 print(food)
#foods[0]='shit' Doen't work.
foods=('burger','french fries','coffee','salad','pizza')
for food in foods:
 print(food)