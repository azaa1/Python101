# Sample project: 2
# Lets say we have 1 database for 'employees' and another for 'projects'
# We know 'employee' with id 101, who completed 'project' 1
# We need to find the 'name' of the employee and 'name' of the project
# using 'if' statement.

# This is the employee database (dictionary 1)
dic1={'fname': 'Sam', 'lname': 'Carter', 'employee-id': 101, 'dept': 'sales'}
# This is project database (dictionary 2)
dic2={'project-id': 1, 'project-name': 'Car-Sales', 'client': 'Bob'}
if dic1['employee-id'] == 101 and dic2['project-id'] == 1:
    print ('Agent:', dic1['fname'])
    print ('Project:', dic2['project-name'])
