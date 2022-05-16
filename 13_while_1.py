#while loop
current_number=1
while current_number<=5:
 print(current_number)
 current_number=current_number+1

#choose when to quit
prompt="\nTell me sth,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end this program."
message=""
while message!="quit":
    message=input(prompt)
    if message!='quit':
     print(message)

#choose when to quit by flag
prompt="\nTell me sth,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end this program."
active=True

while active:
    message=input(prompt)

    if message=="quit":
        active=False
    else:
        print(message)

#use break to quit while loop
prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"

while True:
    city=input(prompt)

    if city=="quit":
        break
    else:
        print(f"I'd love to go to {city.title()}.")

#use continue in loop
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#avoid infinite loop
x=1
while x<=5:
    print(x)
    x=x+1 #forget 

#pratice 7-4-1
prompt="\nTell me which topping would you like to add:"
prompt+="\nEnter quit when you finished your order."
toppings=[]
while True:
    topping=input(prompt)
    if topping=="quit":
        break
    else:
        print(f"\n{topping.title()} has been added to your pizza,enjoy!")
        toppings.append(topping)
if toppings!=[]:
    print("\nHere is your order,pizza with:")
    for chosen_topping in toppings:
        print(f"\n{chosen_topping.title()}")

#pratice 7-4-2
prompt="\nTell me which topping would you like to add:"
prompt+="\nEnter quit when you finished your order."
toppings=[]
active=True
while active:
    topping=input(prompt)
    if topping=="quit":
        active=False
    else:
        print(f"\n{topping.title()} has been added to your pizza,enjoy!")
        toppings.append(topping)
if toppings!=[]:
    print("\nHere is your order,pizza with:")
    for chosen_topping in toppings:
        print(f"\n{chosen_topping.title()}")

#pratice 7-5
prompt="Please enter your age:"
age=""
while age!="quit":
    age=input(prompt)
    if age.isdigit()==True:
        age=int(age)
        if age<3:
            print("You can watch the movie for free.")
        elif age<=12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    elif age!="quit":
        print("input error.")
print("The system is closed.")