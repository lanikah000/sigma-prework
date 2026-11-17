from datetime import datetime

dob = input("Please enter your date of birth (DD-MM-YYYY): ")
dob_list = dob.split("-")
day = int(dob_list[0])
month = int(dob_list[1])
year = int(dob_list[2])

def age_calculator(day, month, year):
    current = datetime.now()
    age = current.year - year
    if month > current.month:
        age -= 1
    elif month == current.month and day > current.day:
        age -= 1
    return age

print(age_calculator(day, month, year))