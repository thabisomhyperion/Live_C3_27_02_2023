'''
Student Class
'''
class Student:
	'''Constructor: first function that is execute when an object is created'''

	def __init__(self, name, surname, contacts):
		self.stud_name = name  # attribute (stud_name) assigned value of parametor(name)
		self.stud_surname = surname
		self.stud_contacts = contacts

	def get_contact(self):
		return self.stud_contacts
		
	def to_the_file(self):
		return f"{self.stud_name},{self.stud_surname},{self.stud_contacts}"

	def get_fullnames(self):
		return f"{self.stud_surname} {self.stud_name}"

	def __str__(self):
		return f"""--------------
Student Name: {self.stud_name}
Student Surname: {self.stud_surname}
Student Contact: {self.stud_contacts}
-------------"""
