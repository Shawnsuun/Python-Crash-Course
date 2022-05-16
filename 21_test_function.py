#test function
def get_formatted_name(first,last):
	full_name=f"{first} {last}"
	return full_name.title()

#passable test
import unittest

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

#unpassable test
def get_formatted_name(first,middle,last):
	full_name=f"{first} {middle} {last}"
	return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

#adjust to pass
def get_formatted_name(first,last,middle=''):
	if middle:
		full_name=f"{first} {middle} {last}"
	else:
		full_name=f"{first} {last}"
	return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

#add a new test
def get_formatted_name(first,last,middle=''):
	if middle:
		full_name=f"{first} {middle} {last}"
	else:
		full_name=f"{first} {last}"
	return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

	def test_first_middle_last_name(self):
		formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

#pratice 11-1
def get_formatted_city_name(city,country):
	formatted_city_name=f"{city},{country}"
	return formatted_city_name.title()

#pratice 11-2
def get_formatted_city_name(city,country,population=''):
	if population:
		formatted_city_name=f"{city},{country}-population:{population}"
	else:
		formatted_city_name=f"{city},{country}"
	return formatted_city_name.title()

class CityNamesTestCase(unittest.TestCase):
	
	def test_city_name(self):
		formatted_city_name=get_formatted_city_name('new york','united states of america')
		self.assertEqual(formatted_city_name,'New York,United States Of America')
	
	def test_city_name_population(self):
		formatted_city_name=get_formatted_city_name('new york','united states of america',8000000)
		self.assertEqual(formatted_city_name,'New York,United States Of America-Population:8000000')

if __name__=='__main__':
	unittest.main()