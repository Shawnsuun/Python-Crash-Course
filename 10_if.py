cars=['audi','bmw','subaru','toyota']
for car in cars:
 if car=='bmw':
  print(car.upper())
 else:
  print(car.title())

car='Audi'
print(car=='audi')
print(car.lower()=='audi')

requested_topping='mushroom'
if requested_topping!='anchovies':
 print("Hold the anchovies!")

 age=18
 print(age==18)

 answer=17
 if answer!=42:
  print("This is not the correct answer,please try again!")

#check multi conditions(and)
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)

age_1=22
print(age_0>=21 and age_1>=21)

#check multi conditions(or)
age_0=22
age_1=18
print(age_0>=21 or age_1>=21)

age_0=18
print(age_0>=21 or age_1>=21)

#check if sth included in the list
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('apple' in requested_toppings)

#check if sth not included in the list
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
  print(f"{user.title()},you can post a response if you wish.")

#pratice 5-1
car='subaru'
print("Is car=='subaru'?I predict True.")
print(car=='subaru')
print("\nIs car=='benz'?I predict False.")
print(car=='benz')

#pratice 5-2
my_favorite_number=2
friend_favorite_number=2
print("Is it the same number?")
print(my_favorite_number==friend_favorite_number)

star='Jay'
print(star.lower()==star)

gender_1=1
gender_2=0
print(gender_1!=gender_2)
print(gender_1==gender_2)
print(gender_1>=gender_2)
print(gender_1<=gender_2)

print(gender_1==1 and gender_2==1)
print(gender_1==1 or gender_2==1)

banned_users=['andrew','carolina','david']
user='andrew' 
if user in banned_users:
 print(f"{user.title()},please leave!")
user='shawn'
if user not in banned_users:
 print(f"Hello {user.title()},welcome!")

#if-else sentense
age=15
if age>=18:
 print("You're old enough to vote!")
 print("Have you registered! to vote yet?")
else:
 print("Sorry,you're too young to vote!")
 print("Please register to vote as soon as you turn 18!")

#if-elif-else structure
age=12
if age<4:
 print("Your admission cost is $0.")
elif age<18:
 print("Your admission cost is $25.")
else:
 print("Your admission cost is $40.")

#multi if-elif-else structure
age=68
if age<4:
 price=0
elif age<18:
 price=25
elif age<65:
 price=45
else:
 price=20
print(f"Your admission cost is ${price}.")

#omit else
age=68
if age<4:
 price=0
elif age<18:
 price=25
elif age<65:
 price=45
elif age>=65:
 price=20
print(f"Your admission cost is ${price}.")

requested_toppings=['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
 print("Add mushroom.")
if 'pepperoni' in requested_toppings:
 print("Add pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Add extra cheese.")
print("\nFinished making your pizza!")

#pratice 5-3
alien_color=['green']
if 'green' in alien_color:
 print("You've gained 5 points!")
alien_color=['green']
if 'green' not in alien_color:
 print("You've gained 5 points!")

#pratice 5-4
alien_color='red'
if alien_color=='green':
 print("You've gained 5 points!")
if alien_color!='green':
 print("You've gained 10 points!")

alien_color='red'
if alien_color=='green':
 print("You've gained 5 points!")
else:
 print("You've gained 10 points!") 

alien_color='red'
if alien_color=='green':
 print("You've gained 5 points!")
elif alien_color=='yellow':
 print("You've gained 10 points!")
else:
 print("You've gained 15 points!")

alien_color='green'
if alien_color=='green':
 print("You've gained 5 points!")
elif alien_color=='yellow':
 print("You've gained 10 points!")
else:
 print("You've gained 15 points!")

alien_color='yellow'
if alien_color=='green':
 print("You've gained 5 points!")
elif alien_color=='yellow':
 print("You've gained 10 points!")
else:
 print("You've gained 15 points!")

#pratice 5-6
age=66
if age<2:
 print("infant")
elif age<4:
 print("baby")
elif age<13:
 print("child")
elif age<20:
 print("teen")
elif age<65:
 print("adult")
else:
 print("elder")

#pratice 5-7
favorite_fruits=['apple','banana','pear']
if 'apple' in favorite_fruits:
 print("You really like apples!")
if 'pineapple' in favorite_fruits:
 print("You really like pineapples!")
if 'coconut' in favorite_fruits:
 print("You really like coconuts!")
if 'grape' in favorite_fruits:
 print("You really like grapes!")
if 'banana' in favorite_fruits:
 print("You really like bananas!")

#check sprcific element
requested_toppings=['mushroom','green pepper','extra cheese']
for requested_topping in requested_toppings:
 print(f"Adding {requested_topping}.")
print("\nFinished making your pizza.")

requested_toppings=['mushroom','green pepper','extra cheese']
for requested_topping in requested_toppings:
 if requested_topping=='green pepper':
  print("Sorry,we are out of green peppers right now.")
 else:
  print(f"Adding {requested_topping}.")
print("\nFinished making your pizza.")

#check empty list
requested_toppings=[]
if requested_toppings:
 for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
else:
 print("Are you sure you want a plain pizza?")

available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for topping in requested_toppings:
 if topping in available_toppings:
  print(f"Add {topping}.")
 else:
  print("Sorry, we don't have this topping.")
print("\nFinished making your pizza.")

#pratice 5-8
user_name='admin'
if user_name=='admin':
 print("Hello admin, would you like to see a status report?")
else:
 print(f"Hi {user_name},thank you for your logging in again.")

#pratice 5-9
user_name=['admin','Jack']
if user_name:
 if 'admin' in user_name:
  print("Hello admin, would you like to see a status report?")
  user_name.remove('admin')
  for user in user_name:
   print(f"Hi {user},thank you for your logging in again.")
 else:
  for user in user_name:
   print(f"Hi {user},thank you for your logging in again.")
else:
 print("We need to find some users!")

#pratice 5-10
current_users=['Amy','Becky','candy','daisy','emily']
current_users_lower=[]
for user_lower in current_users:
 current_users_lower.append(user_lower.lower())
print(current_users_lower)
new_users=['Ada','bella','Cathy','Daisy','Emily']
for user in new_users:
 if user.lower() in current_users_lower:
  print(f"The username '{user.title()}' has been used.")
 else:
  print(f"The username '{user.title()}' has not been used.")

#pratice 5-11
numbers=[]
for number in range(1,10):
 numbers.append(number)
 if number==1:
  order='st'
 elif number==2:
  order='nd'
 elif number==3:
  order='rd' 
 else:
  order='th'
 print(f"{number}{order}")