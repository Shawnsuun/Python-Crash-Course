#a simple dictionary
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points=alien_0['points']
print(f"you just earned {new_points} points!")

#add key-value pair
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#empty dictionary
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#change value in dictionary
print(f"The alien is {alien_0['color']}.")
alien_0['color']='yellow'
print(f"The alien is {alien_0['color']}.")

alien_0={'x_position': 0, 'y_position': 25,'speed':'medium'}
print(f"Oringinal position:{alien_0['x_position']}")

#alien right move
if alien_0['speed']=='slow':
 x_increment=1
elif alien_0['speed']=='medium':
 x_increment=2
else: 
 x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print(f"New x-position:{alien_0['x_position']}")

#delete key-value pair in dictionary
alien_0={'color':'green','points':5}
del(alien_0['points'])
print(alien_0)

favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
language=favorite_language['sarah']
print(f"Sarah's favorite language is {language}.")

#get to access
alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point value assigned')
print(point_value)

#pratice 6-1
contacts_0={'first_name':'Jim','last_name':'Kerry','age':18,'city':'New York'}
print(contacts_0['first_name'])
print(contacts_0['last_name'])
print(contacts_0['age'])
print(contacts_0['city'])

#pratice 6-2
favorite_number={'Amy':3,'Bell':5,'Sandy':6,'Cloud':0,'Frank':4}
print("Amy,what is your favorite number?")
favorite_number_0=favorite_number['Amy']
print(favorite_number_0)
print("is it true?")
print(favorite_number_0==favorite_number['Amy'])

print(favorite_number['Bell'])
print("Bell,what is your favorite number?")
favorite_number_1=favorite_number['Amy']
print(favorite_number_1)
print("is it true?")
print(favorite_number_1==favorite_number['Bell'])

print(favorite_number['Sandy'])
print(favorite_number['Cloud'])
print(favorite_number['Frank'])

#pratice 6-3
codes={'for':'use it to loop','if':'check different conditions'}
print(codes['for'])
print(f"\n{codes['if']}")

#for loop dictionary
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for k,v in user_0.items():
 print(f"\nkey:{k}")
 print(f"value:{v}")

favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for n,l in favorite_language.items():
 print(f"{n.title()}'s favorite language is {l.title()}.")

#for loop keys in dictionary
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_language.keys():
 print(name.title())

friends=['phil','sarah']
for name in favorite_language.keys():
 print(f"Hi,{name.title()}.")
 if name in friends:
  language=favorite_language[name].title()
  print(f"\t{name.title()},I see you love {language}!")

 if 'erin' not in favorite_language.keys():
  print("Erin,please take our poll!")

#sort the dictionary
for name in sorted(favorite_language.keys()):
 print(f"{name.title()},thank you for taking the poll.")

#use in set to delete repetitive items
print("The following languages have been mentioned.")
for language in set(favorite_language.values()):
 print(language.title())

#auto delete repetitive items in collection
languages={'python', 'c', 'ruby', 'python'}
print(languages)

#pratice 6-4
codes={'for':'use it to loop','if':'check condition','else':'another condition'}
for code,explain in codes.items():
 print(f"\n{code}")
 print(explain)
codes['del']='delete an element'
codes['append']='add an element'
for code,explain in codes.items():
 print(f"\n{code}")
 print(explain)

#pratice 6-5
rivers={'nile':'eygpt','times':'england','yangzi':'china'}
for name,country in rivers.items():
 print(f"The {name.title()} runs through {country.title()}.")
for name in rivers.keys():
 print(name.title())
for country in rivers.values():
 print(country.title())

#pratice 6-6
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
poll_candidates=['jen','jack','phil','colin']
for person in poll_candidates:
 if person in favorite_language.keys():
  print(f"{person.title()},thank you for taking the poll!")
 else:
  print(f"{person.title()},we invite you to take a poll.")

#nest(dictionaries in list)
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
 print(alien)

#create 30 aliens
aliens=[]
for alien_number in range(30):
 new_alien={'color':'green','points':5}
 aliens.append(new_alien)
for alien in aliens[:5]:
 print(alien)
print(f"total number of aliens:{len(aliens)}")

#alter first 3 aliens
aliens=[]
for alien_number in range(30):
 new_alien={'color':'green','points':5,'speed':'slow'}
 aliens.append(new_alien)
for alien in aliens[:3]:
 if alien['color']=='green':
  alien['color']='yellow'
  alien['speed']='medium'
  alien['points']=10
for alien in aliens[:5]:
 print(alien)
print(f"total number of aliens:{len(aliens)}")

for alien in aliens[:3]:
 if alien['color']=='green':
  alien['color']='yellow'
  alien['speed']='medium'
  alien['points']=10
 elif alien['color']=='yellow':
  alien['color']='red'
  alien['speed']='fast'
  alien['points']=15 
for alien in aliens[:5]:
 print(alien)
print(f"total number of aliens:{len(aliens)}")

#list in dictionary
pizza={
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
    }
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings")
for topping in pizza['toppings']:
    #print(f"\t{topping}")   
    print("\t"+topping)

favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
    }
for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
     print("\t"+language.title())

#save dictionary in dictionary
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }    
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location'].title()
    print(f"Full name:{full_name.title()}")
    print(f"Location:{location.title()}")

#pratice 6-7
contacts_0={'first_name':'Jim','last_name':'Kerry','age':18,'city':'New York'}
contacts_1={'first_name':'Kim','last_name':'Kardaishan','age':29,'city':'Los Angeles'}
contacts_2={'first_name':'Kenya','last_name':'West','age':32,'city':'Tokyo'}
people=[contacts_0,contacts_1,contacts_2]
for contact in people:
 print(f"\n{contact['first_name']}")
 print(contact['last_name'])
 print(contact['age'])
 print(contact['city'])

#pratice 6-8
pet_1={'category':'cat','owner':'Ian'}
pet_2={'category':'dog','owner':'Shawn'}
pet_3={'category':'piggy','owner':'Bloom'}
pets=[pet_1,pet_2,pet_3]
for pet in pets:
 print(f"{pet['owner'].title()}'s pet is a {pet['category']}.")

#pratice 6-9
favorite_places={'Shawn':
    ['Interlaken','Miami'],
    'Sarah':
    ['Beijing','Hongkong','new york'],
    'Seth':
    ['Tokyo','Kyoto']
    }
for name,places in favorite_places.items():
    print(f"\nName:\n\t{name.title()}")
    print(f"Favorite places:")
    for place in places:
        print(f"\t{place.title()}")

#pratice 6-10
favorite_number={'Amy':3,'Bell':5,'Sandy':6,'Cloud':0,'Frank':4}
for name,number in favorite_number.items():
 print(f"\nName:{name.title()}")
 print(f"Favorite number:{number}")

#pratice 6-11
cities={
    'Beijing':
    {'country':'China','population':'20 million'},
    'New York':
    {'country':'USA','population':'8 million'},
    'London':
    {'country':'USA','population':'8 million'}
    }
for city,info in cities.items():
    print(f"\nCityName:{city}")
    for key,value in info.items():
        print(f"{key.title()}:{value}")