#Chapter-10
#Files and Exceptions
#Reading Files
file_path = 'pi_digit.txt'
with open(file_path) as file_container:
	content = file_container.read()
	print(content.strip())

#File Path
#with open('text_files\filename.txt') as file_object: => Relative path
#file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt' => Absolute path
#with open(file_path) as file_object:

#Read file line by line
file_path = "pi_digit.txt"
with open(file_path) as file_container:
	for line in file_container:
		print(line.strip())

#Making a List of Lines from a File
#readlines => this method will help u to store a contents in a list
file_path = "pi_digit.txt"
with open(file_path) as file_container:
	lines = file_container.readlines()

for line in lines:
	print(line.rstrip())

#Working with file contents
file_path = "pi_digit.txt"
with open(file_path) as file_container:
	lines = file_container.readlines()

pi_digit = ""
for line in lines:
	pi_digit += line.strip()

print(pi_digit)
print(len(pi_digit))

#Large file-One million digits
print(pi_digit[:52] + "....")

#Is my bday date in pi_digits
file_path = "pi_digit.txt"
with open(file_path) as file_container:
	lines = file_container.readlines()

pi_digit = ""
for line in lines:
	pi_digit += line.strip()

print(pi_digit)
print(len(pi_digit))

#bday = input("Enter a bday details in format of DDMMYY: " )
#if bday in pi_digit:
	#print("Yes.... " + " yor bday ther in pi_digit")
#else:
	#print("Sorry!!!! " + " Not there")

#Ass-1
with open("learn_python.txt") as file_container:
	content = file_container.read()
	print(content)

with open("learn_python.txt") as file_container:
	for content in file_container:
		print(content.strip())

with open("learn_python.txt") as file_container:
	content = file_container.readlines()
	print(content)

with open("learn_python.txt") as file_container:
	content = file_container.readlines()

sentence = ""
for contents in content:
	sentence += "My statement: " + contents	
print("\n" + sentence.strip())

#Ass-2
#replace method
with open("learn_python.txt") as file_container:
	content = file_container.read()
	print(content.replace('mahi', 'krishna'))

#Writing a file
#Writing a empty file
#file_path = "program.txt"

#with open(file_path, "w") as file_container:
	#file_container.write("my name is mahi\n")
#Multi lines
	#file_container.write("my fav language is python")

#Appending to file
#file_path = "program.txt"

#with open(file_path, "a") as file_container:
	#file_container.write("my msg: good morning")

#Exceptions
#Using try-except blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("we can't divide 5 by 0")

#Using Exceptions to prevent crashes
#The else block
while True:
	num1 = input("Enter your 1st number: ")
	if num1 == "q":
		break
	num2 = input("Enter your 2nd number: ")
	try:
		ans = int(num1)/int(num2)
	except ZeroDivisionError:
		print("we can't divide 5 by 0")
	else:
		print(ans)

#Handling the FileNotFoundError Exception
f_name = "alice.txt"

try:
	with open(f_name) as file_container:
		content = file_container.read()

except FileNotFoundError:
	print("the file name doesn't exist")

#Analysing the text
f_name = "learn_python.txt"

try:
	with open(f_name) as file_container:
		content = file_container.read()

except FileNotFoundError:
	print("This file doesn't exist")

else:
	split_words = content.split()
	print(len(split_words))

#Working with multiple files
def count_words(f_name):
	"""count the approximate number in the files"""
	try:
		with open(f_name) as file_container:
			content = file_container.read()
	
	except FileNotFoundError:
		print("This file doesn't exist")

	else:
		split_words = content.split()
		print(len(split_words))

f_names = ["alice.txt", "learn_python.txt"]
for f_name in f_names:
	count_words(f_name)

#Failing silently - Pass statement
def count_words(f_name):
	"""count the approximate number in the files"""
	try:
		with open(f_name) as file_container:
			content = file_container.read()
	
	except FileNotFoundError:
		pass

	else:
		split_words = content.split()
		print(len(split_words))

f_names = ["alice.txt", "learn_python.txt"]
for f_name in f_names:
	count_words(f_name)

#Ass-1
try:
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter a number: "))
	ans = int(num1) + int(num2)
	print(ans)

except ValueError:
	print("Please enter a numerical vaule to do addiction")

#Ass-2
"""While Loop to continue the program"""
while True:
	try:
		num1 = input("Enter a number: ")
		num2 = input("Enter a number: ")
		if num1 == "q":
			break
		ans = int(num1) + int(num2)

	except ValueError:
		print("Please enter a numerical vaule to do addiction")

	else:
		print(ans)

#Ass-3
try:
	with open("alice.txt") as file_container:
		content = file_container.read()
		print(content)

except FileNotFoundError:
	print("Sorry!!!.....This file doesn't exist")

#Ass-4
def count_words(f_name):
	try:
		with open(f_name) as file_container:
			content = file_container.read()
			print(content)

	except FileNotFoundError:
		pass

f_names = [ "alice.txt", "learn_python.txt"]
for f_name in f_names:
	count_words(f_name)

#Ass-5
try:
	with open("learn_python.txt") as file_container:
		content = file_container.read()

except FileNotFoundError:
	print("Sorry!...This file doesn't exist")

else:
	total = content.lower().count("the")
	print(total)

#Storing Data
#JSON - JavaScript Object Notation
#Using json.dump() 
import json

numbers = [2,4,6,8]
f_name = "numbers.json"

with open(f_name, "w") as file_container:
	json.dump(numbers, file_container)

#Using json.load()
import json

f_name = "numbers.json"
with open(f_name) as file_container:
	content = json.load(file_container)

	print(content)

#Saving user-generated data
import json

name = input("Enter your name: ")
f_name = "user.json"
with open(f_name, "w") as file_container:
	json.dump(name, file_container)
	print("We will remember you when you will come back " + str(name))

#Reading user-generated data
import json
f_name = "user.json"
with open(f_name) as file_container:
	greeting = json.load(file_container)
	print("Welcome back " + str(greeting))

#Joined both programs
import json
f_name = "mahi.json"
try:
	with open(f_name) as file_container:
		greeting = json.load(file_container)

except FileNotFoundError:
	name = input("Enter your name: ")
	with open(f_name, "w") as file_container:
		json.dump(name, file_container)
		print("We will remember you when you will come back " + str(name))

else:
	print("Welcome back " + str(greeting))

#Refactoring
import json
def greet_user():
	"""Greet the user by name"""
	f_name = "mahi.json"
	try:
		with open(f_name) as file_container:
			greeting = json.load(file_container)

	except FileNotFoundError:
		name = input("Enter your name: ")
		with open(f_name, "w") as file_container:
			json.dump(name, file_container)
			print("We will remember you when you will come back " + str(name))

	else:
		print("Welcome back " + str(greeting))
greet_user()

#Seperate the function
import json
def get_stored():
	f_name = "mahi.json"
	try:
		with open(f_name) as file_container:
			greeting = json.load(file_container)
	except FileNotFoundError:
		return None
	else:
		return greeting

def greet_user():
	greeting = get_stored()
	if greeting:
		print("Welcome back " + str(greeting))
	else:
		name = input("Enter your name: ")
		with open(f_name, "w") as file_container:
			json.dump(name, file_container)
			print("We will remember you when you will come back " + str(name))

greet_user()

#Again seperate function
import json
def get_stored():
	f_name = "mahi.json"
	try:
		with open(f_name) as file_container:
			greeting = json.load(file_container)
	except FileNotFoundError:
		return None
	else:
		return greeting

def get_new_username():
	"""Prompt for a new username"""
	f_name = "mahi.json"
	name = input("Enter your name: ")
	with open(f_name, "w") as file_container:
		json.dump(name, file_container)
	return greeting

def greet_user():
	greeting = get_stored()
	if greeting:
		print("Welcome back " + str(greeting))
	else:
		greeting = get_new_username()
		print("We will remember you when you will come back " + str(name))

greet_user()

#Ass-1
import json

num = input("Enter a number: ")
f_name = "fav_num.json"
with open(f_name, "w") as file_container:
	json.dump(num, file_container)

import json

f_name = "fav_num.json"
with open(f_name) as file_container:
	fav_number = json.load(file_container)
	print(fav_number)

#Ass-2
import json
try:
	f_name = "my_fav.json"
	with open(f_name) as file_container:
		fav_number = json.load(file_container)

except FileNotFoundError:
	num = input("Enter a number: ")
	with open(f_name, "w") as file_container:
		json.dump(num, file_container)
		print("i will save your fav number")

else:
	print("I know your fav number " + str(fav_number))

#Ass-3
import json
def get_stored():
	f_name = "mahi.json"
	try:
		with open(f_name) as file_container:
			greeting = json.load(file_container)
	except FileNotFoundError:
		return None
	else:
		return greeting

def get_new_username():
	"""Prompt for a new username"""
	f_name = "mahi.json"
	name = input("Enter your name: ")
	with open(f_name, "w") as file_container:
		json.dump(name, file_container)
	return greeting

def greet_user():
	greeting = get_stored()
	if greeting:
		correct = input("Are you " + str(greeting) + "? (y/n) ")
		if correct == "y":
			print("Welcome back " + str(greeting))
		else:
			greeting = get_new_username()
			print("We will remember you when you will come back " + str(name))

	else:
		greeting = get_new_username()
		print("We will remember you when you will come back " + str(name))

greet_user()