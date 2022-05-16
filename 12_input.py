message=input("Tell me sth, and I'll repeat it back to you:")
print(message)

prompt="If you tell us who you are, we can personalize the message you see."
prompt+="\nwhat is your first name?"
name=input(prompt)
print(f"\nHello,{name}!")

#input string to number
age=input("How old are you?")
age=int(age)
print(age>=18)

height=input("How tall are you?")
height=int(height)
if height>=48:
 print("\nYou are tall enough to ride!")
else:
 print("\nYou'll be able to ride when older.")

number=input("Enter a number and I'll tell you if it is even or odd:")
number=int(number)
if number%2==0:
 print(f"The number {number} is even.")
else:
 print(f"The number {number} is odd.")

#pratice 7-1
car=input("Which kind of car do you want to rent?")
print(f"Let me see if I can find you a {car}.")

#pratice 7-2
customer_number=input("What's the number of dinning people?")
customer_number=int(customer_number)
if customer_number>8:
 print("Sorry, there are no tables available.")
else:
 print("Welcome, there are tables available.")

#pratice 7-3
number=input("Please input a number, I'll tell you if it is mutiples of 10!")
number=int(number)
if number%10==0:
 print(f"The number {number} is mutilples of 10.")
else:
 print(f"The number {number} is not mutilples of 10.") 