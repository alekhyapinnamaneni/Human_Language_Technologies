# Alekhya Pinnamaneni
# axp190109
# CS 4395.001

import sys
import pathlib
import re
import pickle


# Person Class
class Person:
    def __init__(self, last, first, mi, person_id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.person_id = person_id
        self.phone = phone

    def display(self):
        print("\nEmployee id: ", self.person_id)
        print("\t", self.first, self.mi, self.last)
        print("\t", self.phone)


# Function name: process_lines
# Function: converts data in data.csv into a dict of Person objects, modifying any incorrect fields
# Input: a list of strings representing each line in the data.csv file
# Output: a dict of Person objects
def process_lines(lines):
    employees_dict = {}
    for line in lines:
        # Modify first and last names to be in Capital Case
        curr_last, curr_first, curr_mi, curr_id, curr_phone = line.split(",")
        curr_first = curr_first[0].upper() + curr_first[1:].lower()
        curr_last = curr_last[0].upper() + curr_last[1:].lower()
        # Capitalize middle initial, "X" if no middle initial is given
        if curr_mi == "":
            curr_mi = "X"
        else:
            curr_mi = curr_mi.upper()
        # Request user to re-enter ID if invalid
        if not re.match('^[A-Z][A-Z][0-9][0-9][0-9][0-9]$', curr_id):
            print("ID invalid: ", curr_id)
            print("ID is two letters followed by 4 digits")
            print("Please enter a valid ID: ", end="")
            curr_id = input()
        # Modify phone number to correct format and request user to re-enter phone number if invalid
        if re.match('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', curr_phone):
            curr_phone = curr_phone[0:3] + "-" + curr_phone[3:6] + "-" + curr_phone[6:]
        elif re.match('^[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9][0-9]$', curr_phone):
            curr_phone = curr_phone[0:3] + "-" + curr_phone[4:7] + "-" + curr_phone[8:]
        elif re.match('^[0-9][0-9][0-9][.][0-9][0-9][0-9][.][0-9][0-9][0-9][0-9]$', curr_phone):
            curr_phone = curr_phone[0:3] + "-" + curr_phone[4:7] + "-" + curr_phone[8:]
        else:
            print("Phone ", curr_phone, "is invalid")
            print("Enter phone number in form 123-456-7890")
            print("Please enter phone number: ", end="")
            curr_phone = input()
        # Create Person object and add to dict
        curr_employee = Person(curr_last, curr_first, curr_mi, curr_id, curr_phone)
        employees_dict[curr_id] = curr_employee
    return employees_dict


if __name__ == "__main__":
    # Check if user provided file path as a sys arg and quit program if not
    if len(sys.argv) < 2:
        print("Please enter a filename as a system arg")
        quit()

    # Open and read file line by line using file path provided in sys arg
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

    # Call function to process lines and save dict in 'employees' variable
    employees = process_lines(text_in[1:])

    # Save dict as a pickle file
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # Open and read pickle file
    employees_in = pickle.load(open ('employees.pickle', 'rb'))

    # Print employee list from pickle file
    print('\n\nEmployee list:')

    for emp_id in employees_in.keys():
        employees_in[emp_id].display()  # Print employee info using Person class's display() function
