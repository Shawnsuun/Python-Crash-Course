#read file
with open('pi_digits.txt') as file_object:
	contents=file_object.read()
print(contents.rstrip())

#file relative path
with open('text_files/pi_digits.txt') as file_object:
	contents=file_object.read()
print(contents.rstrip())

#file absolute path
file_path='C:/Users/Sunxw/Desktop/python_work/text_files/pi_digits.txt'
with open(file_path) as file_object:
	contents=file_object.read()
print(contents.rstrip())

#read by line
file_name='pi_digits.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

#create a list with element from each line
file_name='pi_digits.txt'
with open(file_name) as file_object:
	lines=file_object.readlines()
print(lines)
for line in lines:
	print(line.rstrip())

#use file content
file_name='pi_digits.txt'
with open(file_name) as file_object:
	lines=file_object.readlines()

#delete right side blank
pi_string=''
for line in lines:
	pi_string+=line.rstrip()

print(pi_string)
print(len(pi_string))

#delete all the blanks
pi_string=''
for line in lines:
	pi_string+=line.strip()

print(pi_string)
print(len(pi_string))

#million digits
file_name='pi_million_digits.txt'
with open(file_name) as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.strip()
print(pi_string)
print(len(pi_string))

#find your birthday in pi
#birthday=input("Enter your birthday, in the form of mmddyy:")
#not working in sublineREPL, need to find the reason.
birthday='920906'
if birthday in pi_string:
	print("Your birthday is in the first million digits of pi!")
else:
	print("Your birthday is not in the first million digits of pi, please try again.")

#pratice 10-1
file_name='learning_python.txt'
with open(file_name) as file_object:
	contents=file_object.read()
print(contents.rstrip())

with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(file_name) as file_object:
	list=file_object.readlines()
print(list)
for sentense in list:
	print(sentense.rstrip())

#pratice 10-2
with open(file_name) as file_object:
	list=file_object.readlines()
print(list)
for sentense in list:
	sentense=sentense.replace('Python','C')
	print(sentense.rstrip())

#write multi lines in file
file_name='programming.txt'
with open(file_name,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

#add to file
file_name='programming.txt'
with open(file_name,'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

#pratice 10-3, 10-4, 10-5
file_name='guest.txt'
while True:
	guest_name=input("Please enter your name(Enter 'quit' to exit or 'clear' to reset):")
	if guest_name=='clear':
		with open(file_name,'w') as file_object:
			file_object.write("")
	elif guest_name=='quit':
		break
	else:
		with open(file_name,'a') as file_object:
			print(f"Hello,{guest_name.title()}!")
			file_object.write(f"Name:{guest_name.title()}\n")
			reason=input("The reason why you like programming is:")
			file_object.write(f"Reason:{reason}\n")

#Try-execpt to avoid reporting error
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#Try-execpt-else module
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to exit")
while True:
	first_number=input("\nFirst Number:")
	if first_number=='q':
		break
	second_number=input("Second Number:")
	if second_number=='q':
		break
	try:
		answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)

#filenotfound error
file_name='alice.txt'
try:
	with open(file_name,encoding='utf-8') as f:
		contents=f.read()
except FileNotFoundError:
	print("File not exist.")
else:
	print(contents)