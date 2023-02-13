"""
Due to the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iterate through the dictionary to print out their name and their new salary (as in image)
"""

import csv

# open the file
infile = open("employee_data.csv", "r")
employee_data = csv.reader(infile)


# create an empty dictionary
sal_dict = {}
employee_name = ""


# use a loop to iterate through the csv file
for employee in employee_data:
    # check if the employee fits the search criteria
    if employee[3] == "Marketing" and employee[4] == "CSR":
        print(
            "Manager Name: ",
            employee[1],
            " ",
            employee[2],
            " Current Salary: $",
            format(float(employee[5]), ",.2f"),
            sep="",
        )
        employee_name = employee[1] + " " + employee[2]
        sal_dict[employee_name] = float(employee[5]) * 1.1


print()
print("=========================================")
print()

# iterate through the dictionary and print out the key and value as per printout
for k, v in sal_dict.items():
    print(f"Manager Name: {k} New Salary: ${v:,.2f}")
