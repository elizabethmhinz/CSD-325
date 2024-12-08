# Program created for CSD325-A339 by Liz Hinz
import json
from os import path

filename = '/Users/Liz/csd/CSD-325/student.json'
listObj = []

# check if file exists
if not path.isfile(filename) or path.getsize(filename) == 0:
    raise Exception('File not found or is empty')

# Load students from student JSON
with open(filename) as fp:
    try:
        listObj = json.load(fp)
    except json.JSONDecodeError:
        raise Exception('Error decoding JSON. Ensure the file is valid JSON.')

# Function that loops through the json class & prints student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']} : ID = {student['Student_ID']}', Email = {student['Email']}")

# Output notification to user that this is the original list
print('This is the original Student list: ')
print_students(listObj)

# append my student info with fake ID number
listObj.append({
    "F_Name": "Liz",
    "L_Name": "Hinz",
    "Student_ID": 14142,
    "Email": "emhinz@my365.bellevue.edu"
})

# Output notification to user that this is the original list 
print('\nThis is the updated Student list:')
print_students(listObj)

# Use dump() function to append the new data to json file
with open(filename, 'w') as json_file: 
    json.dump(listObj, json_file, indent=4, separators=(',',': '))

# Output notification that the json file was updated 
print('Successfully appended to the JSON file')