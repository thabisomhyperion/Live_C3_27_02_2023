'''
Capstone IV - OOP
=> Classes and Objects
=> Files
=> Manipulating data using Objects and Files including List
=> Functions

Santhy Tamang
3:19 PM
is Student after the print command related to the first line of from Student import Student?
'''
from Students import Student

student_list = []
'''
This function is dedicated to read data from the file and used that data to create Student Object and add it to the list(student_list).
'''


def read_file():
  with open('student_data.txt', 'r') as stud_file:
    for line in stud_file:
      name, surname, cont = line.strip('\n').split(',')
      student_list.append(Student(name, surname, cont))


def write_tofile():
	with open('student_data.txt', 'w') as stude_file:
		str_data  = [stud.to_the_file() for stud in student_list]
		stude_file.write('\n'.join(str_data))


'''
itterate over the list and print out all the object in the list.
'''


def view_all():
  for stud in student_list:
    print(stud)


'''
A function that allows us to create and object of the student through user input/keyboard input
'''


def capture_stud():
	name, surname, cont = input("Name: "), input("Surname: "), input(
    "Contacts: ")
	student_list.append(Student(name, surname, cont))  #appending an object
	write_tofile() #Update the file


read_file()

capture_stud()
view_all()
