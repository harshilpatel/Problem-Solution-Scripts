import subprocess
import os

class person:
    age = 0
    first_name = last_name = address = city = ''
    def __init__(self, age, first_name, last_name, address, city):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
    def print_object(self):
    	return 'Person: ' + ' '.join([self.first_name, self.last_name, self.age, self.city, self.address])

a = raw_input('Create a new Person? ')
if a in ['yes','ya']:
	p = person(raw_input("Enter age: "), raw_input("Enter FirstName:  "), raw_input('Enter LastName: '), raw_input('Enter Address: '), raw_input('Enter City:'))
	print p.print_object()