# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         # Read data into dictionary and create a new email field

        # YOUR CODE HERE
        # Hint: You can use csv.DictReader
        # This will require a little bit of independent research (by design)
        # In the real world, you will encounter situations like this
        
        print(str(row['first_name'], row['last_name'],row['ssn']))

    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
        csvwriter.writerow(['Email'])
       

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    # YOUR CODE HERE
    # Hint: You can use csv.DictWriter
    reader = csvpath.DictWriter(csvpath)
    for row in reader: 
        new_employee_data.append(row) 
        new_employee_data.append(['email'] = row[0]+row[1]+"@gmail.com") 
        print(row['first_name'], row['last_name'], row['ssn'], row['email'])
        
        new_employee_data = NewDict([('first_name'), ('last_name'), ('ssn'), ('email')])
        
        writer = csv.DictWriter(csvpath, "w", new_employee_data)
     