#list
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#extrack from list
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message=f"My first bicycle is a {bicycles[0].title()}."
print(message)

names=['abby','berry','candy','daisy','emily']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-2].title())
print(names[-1].title())
message=f"Howdy {names[0].title()}!"
print(message)
message=f"Howdy {names[1].title()}!"
print(message)
message=f"Howdy {names[2].title()}!"
print(message)
message=f"Howdy {names[3].title()}!"
print(message)
message=f"Howdy {names[4].title()}!"
print(message)

motorcycles=['Honda','BMW','Porche','Benz']
message=f"I would like to own a {motorcycles[2]}."
print(message)

#change list element
motorcycles=['Honda','BMW','Porche','Benz']
print(motorcycles)
motorcycles[0]='yamaha'
print(motorcycles)

#add a new element in the list
motorcycles=['Honda','BMW','Porche','Benz']
motorcycles.append('ducati')
print(motorcycles)
motorcycles=[]
motorcycles.append('ducati')
motorcycles.append('Honda')
motorcycles.append('BMW')
motorcycles.append('Porche')
print(motorcycles)

#insert a new element in the list
motorcycles=['Honda','BMW','Porche','Benz']
motorcycles.insert(0,'Ducati')
print(motorcycles)

#delete an element(certain location) in the list
del motorcycles[0]
print(motorcycles)

#pop an element from list
motorcycles=['Honda','BMW','Porche','Benz']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles=['Honda','BMW','Porche','Benz']
last_owned=motorcycles.pop()
print(f"My last motorcycle is {last_owned}.")

motorcycles=['Honda','BMW','Porche','Benz']
first_owned=motorcycles.pop(0)
print(f"My first motorcycle is {first_owned}.")

#delete an element(certain value) in the list
motorcycles=['Honda','BMW','Porche','Benz']
too_expensive='BMW'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#pratice 3-4
candidates=['Abby','Betty','Candy','Daisy']
a=0
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)

#pratice 3-5
pegion=candidates[0]
print(f"Oops, seems {pegion} can not come.")
candidates[0]='Shawn'
a=0
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)

#pratice 3-6
print(candidates)
candidates.insert(0,'Bob')
candidates.insert(2,'Jack')
candidates.append('Dale')
print(candidates)
a=0
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)
a=a+1
message=f"Hey {candidates[a]}, would you like to go for a dinner with me?"
print(message)

#pratice 3-7
print(candidates)
message="Only two persons can be invited."
print(message)
canceled_candidate=candidates.pop()
print(candidates)
canceled_candidate=candidates.pop()
print(f"Sorry {canceled_candidate}, the dinner is canceled.")
canceled_candidate=candidates.pop()
print(f"Sorry {canceled_candidate}, the dinner is canceled.")
canceled_candidate=candidates.pop()
print(f"Sorry {canceled_candidate}, the dinner is canceled.")
canceled_candidate=candidates.pop()
print(f"Sorry {canceled_candidate}, the dinner is canceled.")
a=0
message=f"Hey {candidates[a]}, you are still invited."
print(message)
a=a+1
message=f"Hey {candidates[a]}, you are still invited."
print(message)
del candidates[0]
del candidates[0]
print(candidates)