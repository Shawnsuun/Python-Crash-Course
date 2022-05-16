class AnonymousSurvey:
	def __init__(self,question):
		self.question=question
		self.responses=[]

	def show_question(self):
		print(self.question)

	def store_response(self,new_response):
		self.responses.append(new_response)

	def show_results(self):
		print("Survey Result:")
		for response in self.responses:
			print(f"-{response}")

question={"What language did you first learn to speak?"}
my_survey=AnonymousSurvey(question)

my_survey.show_question
print("Enter 'q' to quit.\n")

while True:
	response=input("Language:")
	if response=='q':
		break
	my_survey.store_response(response)

print("Thank you to everyone who participated the survey!")
my_survey.show_results()

#test class AnonymousSurvey
import unittest

class TestAnoymousSurvey(unittest.TestCase):

	def test_store_single_response(self):
		question={"What language did you first learn to speak?"}
		my_survey=AnonymousSurvey(question)
		my_survey.store_response("English")
		self.assertIn("English",my_survey.responses)

	def test_store_three_responses(self):
		question={"What language did you first learn to speak?"}
		my_survey=AnonymousSurvey(question)
		responses=['English','History','Math']
		my_survey.store_response(responses)
		self.assertIn(responses,my_survey.responses)

#method setUp()
import unittest

class TestAnoymousSurveySetup(unittest.TestCase):

	def setUp(self):
		question={"What language did you first learn to speak?"}
		self.my_survey=AnonymousSurvey(question)
		self.responses=['English','History','Math']

	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn("English",self.my_survey.responses)

	def test_store_three_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:	
			self.assertIn(response,self.my_survey.responses)

#pratice 11-3
class Employee:
	def __init__(self,first_name,last_name,salary):
		self.first_name=first_name
		self.last_name=last_name
		self.salary=salary

	def give_raise(self,salary_raise=5000):
		self.salary+=salary_raise
		return self.salary

import unittest

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.sde=Employee('Shawn','Sun',25000)
		self.salary_raise=15000

	def test_give_defult_raise(self):
		self.assertEqual(30000,self.sde.give_raise())

	def test_give_custom_raise(self):
		self.assertEqual(40000,self.sde.give_raise(self.salary_raise))

if __name__=='__main__':
	unittest.main()