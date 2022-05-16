#function definition
def greet_user():
    print("Hello!")
greet_user()

#username(parameter) and 'jesse'(argument)
def greet_user(username):
    print(f"Hello!{username.title()}.")
greet_user('jesse')

#pratice 8-1
def display_message():
    print("I have learnt knowledge about function definition")
display_message()

#pratice 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")
favorite_book("alice in wonderland")

#locational argument
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog','willie')

#keyword argument
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='willie',animal_type='dog')

#defult value
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet('harry','hamster')
describe_pet(animal_type='hamster',pet_name='harry')

#pratice 8-3
def make_shirt(size,wdprint):
    print(f"The shirt is {size.title()} size with wordprint {wdprint}.")
make_shirt('s','NIKE')
make_shirt('m','Adidas')
make_shirt(wdprint='PUMA',size='l')

#pratice 8-4
def make_shirt(size='l',wdprint='I love Python'):
    print(f"The shirt is {size.title()} size with wordprint {wdprint}.")
make_shirt()
make_shirt('m')
make_shirt(wdprint='Hello')

#pratice 8-5
def describe_city(name,country='iceland'):
    print(f"{name.title()} is in {country.title()}.")
describe_city('Reykjavik')
describe_city('Guangzhou')
describe_city('London')

#return
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

#optional argument
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('jimi','hendrix','lee')
print(musician)

#return dictionary
def build_person(first_name,last_name,age=None):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return(person)
musician=build_person('Jay','Chou',12)
print(musician)
musician=build_person('Jay','Chou')
print(musician)

#function and while loop
def get_formatted_name(first_name,last_name,age=None):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Please tell me your name.")
    print("(Enter 'q' at anytime to quit.)")
    f_name=input("First name:")
    if f_name=='q':
        break
    l_name=input("Last name:")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello!{formatted_name}.")

#pratice 8-6
def city_country(city,country):
    return(f"{city.title()},{country.title()}")
city1=city_country('guangzhou','china')
city2=city_country('new york','america')
print(city1)
print(city2)

#pratice 8-7
def make_album(singer,album_name,number_of_songs=None):
    album={}
    album['singer']=singer
    album['album name']=album_name
    if number_of_songs==None:
        return(album)
    else:
        album['number of songs']=number_of_songs
        return(album)
new_album1=make_album("Jay","December's Chopin",10)
new_album2=make_album("Rihanna","Good girl gone bad")
new_album3=make_album("Will","Wuha")
print(new_album1)
print(new_album2)
print(new_album3)

#pratice 8-8
def make_album(singer,album_name,number_of_songs=None):
    album={}
    album['singer']=singer
    album['album name']=album_name
    return(album)
while True:
    singer=input("Enter singer name:")
    album_name=input("Enter album name:")
    new_album=make_album(singer,album_name,number_of_songs=None)
    print(new_album)
    active=input("continue?(y/n):")
    if active=="n":
        break

#transfer list
def greet_users(names):
    for name in names:
        msg=(f"Hi,{name.title()}!")
        print(msg)

welcome_list=['shawn','lily','jack']
greet_users(welcome_list)

#list revision in function
unprinted_designs=['phone case','robot pendant','dodercahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:   
        current_design=unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs=['phone case','robot pendant','dodercahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#pratice 8-9
def show_messages(message_box):
    for message in message_box:
        print(message)
message_box=['Hi!','Indian MI fans,','Are you ok?']
show_messages(message_box)

#pratice 8-10
def send_message(message_box,sent_message_box=[]):
    message_box.reverse()
    while message_box:
        sending_message=message_box.pop()
        print(f"\nSending message '{sending_message}'...")
        sent_message_box.append(sending_message)
        print(f"Your message '{sending_message}' has been sent.")
    return(sent_message_box)

def print_message(message_box,sent_message):
    print("\nHere are the unsent messages:")
    print(message_box)
    print("\nHere are the sent messages:")
    print(sent_message)

message_box=['Hi!','Indian MI fans,','Are you ok?',"I'm very ok"]
send_message(message_box)
sent_message=send_message(message_box)
print_message(message_box,sent_message)

#pratice 8-11
def send_message(message_box,sent_message_box=[]):
    message_box.reverse()
    while message_box:
        sending_message=message_box.pop()
        print(f"\nSending message '{sending_message}'...")
        sent_message_box.append(sending_message)
        print(f"Your message '{sending_message}' has been sent.")
    print("\nHere are the unsent messages:")
    print(message_box)
    print("\nHere are the sent messages:")
    print(sent_message_box)
message_box=['Hi!','Indian MI fans,','Are you ok?',"I'm very ok"]
send_message(message_box[:])
print("check list message_box")
print(message_box)