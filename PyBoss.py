# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os

file_to_load = os.path.join("employee_data.csv")
file_to_output = os.path.join("new_emp_data.csv")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        emp_ids = emp_ids + [row[0]]
        split_name = row[1].split(" ")
        emp_first_names.append(row['Name'].split(" ")[0])
        emp_last_names.append(row['Name'].split(" ")[1])
        emp_dobs.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        emp_ssns.append('***-**-' + row['SSN'].split('-')[4])
        emp_states.append(us_state_abbrev[row['State']])

new_emp_data = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)
output_file = os.path.join('Output' + str(employee_data) + '.csv')

with open(output_file, 'w') as csvwrite:
    newfile = csv.writer(csvwrite, delimiter = ",")
    newfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    newfile.writerows(new_emp_data)