'''
if applicant has high income AND/OR good credit
    Eligible for loan

AND: both must meet the specified conditions
OR: at least ONE must meat the specified conditions
'''

# LOGICAL OPERATORS
has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# COMPARISON OPERATORS
'''
if temperature is greater than 30
    It's a hot day
otherwise if it's less than 10
    It's a cold day
otherwise
    It's neither hot nor cold
'''

temperature = 30

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''

name = "Ryan"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print(f"Name looks good, {name}")
