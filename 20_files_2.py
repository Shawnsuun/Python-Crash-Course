#analysis text
title="Alice in Wonderland"
print(title.split()) 

#split contents to count words
file_name="Alice.txt"
try:
	with open(file_name,encoding='utf-8') as f:
		contents=f.read()
except FileNotFoundError:
	print("File not exist.")
else:
	words=contents.split()
	num_words=len(words)
	print(f"The file {file_name} has {num_words} words.")

#use multi files
def count_words(file_name):
	try:
		with open(file_name,encoding='utf-8') as f:
			contents=f.read()
	except FileNotFoundError:
		print(f"\nFile {file_name} not exist.")
	else:
		words=contents.split()
		num_words=len(words)
		print(f"\nThe file {file_name} has {num_words} words.")

file_name="Alice.txt"
count_words(file_name)

file_names=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for file_name in file_names:
	count_words(file_name)

#remain silence(pass) to error
def count_words(file_name):
	try:
		with open(file_name,encoding='utf-8') as f:
			contents=f.read()
	except FileNotFoundError:
		pass
	else:
		words=contents.split()
		num_words=len(words)
		print(f"\nThe file {file_name} has {num_words} words.")
for file_name in file_names:
	count_words(file_name)

#pratice 10-6 & 10-7
print("Enter numbers and I will add them together(enter 'q' to quit).")
total=0
while True:
	number=input("Number:")
	if number!='q':
		try:
			number=int(number)
			total+=number
		except ValueError:
			print(f"{number} is not a number, please try again.")
		else:
			print(f"The sum of the numbers is {total}.")
	else:
		print("--Calculation end--")
		break

#pratice 10-8
def print_content(file_name):
	try:
		with open(file_name) as file_object:
			content=file_object.read()
	except FileNotFoundError:
		print(f"Sorry,can not found file {file_name}.")
	else:
		print(content)

file_name='cats.txt'
print_content(file_name)
file_name='dogs.txt'
print_content(file_name)

#pratice 10-9
def print_content(file_name):
	try:
		with open(file_name) as file_object:
			content=file_object.read()
	except FileNotFoundError:
		pass
	else:
		print(content)

file_name='cats.txt'
print_content(file_name)
file_name='dogs.txt'
print_content(file_name)

#pratice 10-10
def count_words_appear(file_name,key_word):
	with open(file_name,encoding='UTF-8') as file_object:
		content=file_object.read()
	appear_time=content.lower().count(key_word.lower())
	print(f"The word {key_word.lower().strip()} appears {appear_time} times in {file_name}.")

file_name='alice.txt'
key_word='ALICE'
count_words_appear(file_name,key_word)

key_word='the '
count_words_appear(file_name,key_word)

#save data by json.dump() 
numbers=[2,3,5,7,11,13]

import json

file_name='numbers.json'
with open(file_name,'w') as f:
	json.dump(numbers,f)

#load data by json.load()
import json

file_name='numbers.json'
with open(file_name) as f:
	numbers=json.load(f)

print(numbers)

#save user data
import json
username=input("What is your name:")
file_name='username.json'
with open(file_name,'w') as f:
	json.dump(username,f)
	print(f"We will remember you when you come back,{username}!")

#load user data
import json
file_name='username.json'
with open(file_name) as f:
	username=json.load(f)
	print(f"Welcome back,{username}!")

#remember me
import json
file_name='username.json'
try:
	with open(file_name) as f:
		username=json.load(f)
except FileNotFoundError:
	print("Data not found, please enter your name.")
	username=input("What is your name:")
	with open(file_name,'w') as f:
		json.dump(username,f)
	print(f"We will remember you when you come back,{username}!")
else:
	print(f"Welcome back,{username}!")

#original structure
import json
def greet_user(file_name):
	try:
		with open(file_name) as f:
			username=json.load(f)
	except FileNotFoundError:
		print("Data not found, please enter your name.")
		username=input("What is your name:")
		with open(file_name,'w') as f:
			json.dump(username,f)
		print(f"We will remember you when you come back,{username}!")
	else:
		print(f"Welcome back,{username}!")

greet_user('username.json')

#restructure
import json

def get_stored_username(file_name):
	try:
		with open(file_name) as f:
			username=json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username(file_name):
	print("Data not found, please enter your name.")
	username=input("What is your name:")
	with open(file_name,'w') as f:
		json.dump(username,f)
	print(f"Username {username} has been saved.")
	return username

def greet_user(file_name):
	username=get_stored_username(file_name)
	if username:
		print(f"Welcome back,{username}!")
	else:
		username=get_new_username(file_name)
		print(f"We will remember you when you come back,{username}!")

greet_user('username.json')

#pratice 10-11
import json

file_name='favorite_number'
favorite_number=input("Tell me your favorite number and I will remember it.")
with open(file_name,'w') as f:
	json.dump(favorite_number,f)
print("Ok,the number is saved!")

with open(file_name) as f:
	favorite_number=json.load(f)
print("Loading from your save...")
print(f"Your favorite number is {favorite_number}.")
	
#pratice 10-12
import json

def load_saved_number(file_name):
	try:
		with open(file_name) as f:
			favorite_number=json.load(f)
	except FileNotFoundError:
		return None
	else:
		print("Loading from your save...")
		return favorite_number

def save_new_number(file_name):
	favorite_number=input("Tell me your favorite number and I will remember it.")
	with open(file_name,'w') as f:
		json.dump(favorite_number,f)
	return favorite_number

def remember_favorite_number(file_name):
	favorite_number=load_saved_number(file_name)
	if favorite_number:
		print(f"Your favorite number is {favorite_number}.")
	else:
		favorite_number=save_new_number(file_name)
		print(f"Ok,the number {favorite_number} is saved, next time you will see it.")

remember_favorite_number('favorite_number')

#pratice 10-13
import json

def get_stored_username(file_name):
	try:
		with open(file_name) as f:
			username=json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username(file_name):
	print("Data not found, please enter your name to register as new user.")
	username=input("What is your name:")
	with open(file_name,'w') as f:
		json.dump(username,f)
	print(f"Username {username} has been saved.")
	return username

def greet_user(file_name):
	username=get_stored_username(file_name)
	if username:
		login_name=input("Please enter your username to confirm:")
		print("Veryfying username...")
		if login_name==username:
			print(f"Welcome back,{username}!")
		else:
			username=get_new_username(file_name)
			print(f"We will remember you when you come back,{username}!")
	else:
		username=get_new_username(file_name)
		print(f"We will remember you when you come back,{username}!")

greet_user('username.json')

#pratice 10-13 another answer

def greet_user(file_name):
	username=get_stored_username(file_name)
	if username==None:
		relogin=True
	elif username==input("Please enter your username to confirm:"):
		print("Veryfying username...")
		relogin=False
	else:
		relogin=True

	if relogin==True:
		username=get_new_username(file_name)
		print(f"We will remember you when you come back,{username}!")
	else:
		print(f"Welcome back,{username}!")		

greet_user('username.json')