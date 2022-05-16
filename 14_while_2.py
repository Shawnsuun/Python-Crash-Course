#move elements in different lists
unconfirmed_users=['alice','brain','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"verifying user:{current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users has benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#delete element of certain value
pets=['dogs','cats','dogs','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#fill dictionary with user input
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb today?")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
print("\n---Poll Result---")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response}.")

#pratice 7-8
sandwich_orders=['egg','ham','chicken']
finished_sandwiches=[]
while sandwich_orders:
    cooked_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(cooked_sandwich)
    print(f"I made your {cooked_sandwich} sandwich.")
print("\n---The following sandwiches have been made---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

#pratice 7-9
sandwich_orders=['pastrami','egg','pastrami','ham','pastrami','chicken']
print(sandwich_orders)
print("Pastrami sandwich has been sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

#pratice 7-10
print("This is a poll about your dream vacation destination.")
polling_result={}
active=True
while active==True:
    name=input("What is your name:")
    destination=input("Where do you want to go:")
    polling_result[name]=destination
    repeat=input("continue?(yes/no):")
    if repeat=='no':
        active=False
print("\nHere is the polling result:")
for name,destination in polling_result.items():
    print(f"{name.title()}'s dream vacation place is {destination.title()}!")