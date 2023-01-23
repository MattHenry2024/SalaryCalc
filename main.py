# Name: Matt Henry
# Date: 01/22/2023
# Program: Salary Calculator
# Description: This program is a basic calculator for users to determine their approximate salary, both unadjusted and
# adjusted. The program begins by welcoming the user, and then asking the user for basic information about their
# employment, including hourly rate, hours worked per week, days worked per week, holidays per year and vacation days
# per year. The program will then multiply days per week by 52 weeks to get number of days worked in a year. Then it
# will approximate the average hours per day worked by dividing hours per week by days per week. Then the program will
# multiply annual salary by multiplying salary, hours, and total working days. Then it will approximate adjusted
# salary by multiplying salary by hours and total working days, and working days has had vacation days and holidays
# subtracted from itself. The program will then display both of these numbers rounded to two decimal points and then
# will end.

DASH_LINE = 40  # this is a variable for separation lines

print('=' * DASH_LINE)  # separation line
print("The Salary Calculator Program")  # welcome the user
print('=' * DASH_LINE)  # separation line

COLUMN_LENGTH = 25  # this creates a uniform looking whitespace

salary_per_hour = float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: "))  # asks the user for salary in hours
hours_per_week = float(input(f"{'Hours per week':.<{COLUMN_LENGTH}}: "))  # asks the user for hours per week worked
days_per_week = float(input(f"{'Days per week':.<{COLUMN_LENGTH}}: "))  # asks the user for days worked per week
holidays_per_year = float(input(f"{'Holidays per year':.<{COLUMN_LENGTH}}: "))  # asks user how many holidays they have
vacation_per_year = float(input(f"{'Vacation days per year':.<{COLUMN_LENGTH}}: "))  # asks user how many vacation days

working_days = days_per_week * 52  # calculates how many working days in one year by multiplying 52 weeks by days worked
hours_per_day = hours_per_week / days_per_week  # calculates average hours per day by div hours by days per week

annual_salary = salary_per_hour * hours_per_day * working_days  # calculates annual salary by * salary by hours & work

# calculates adjusted salary by multiply salary and hours and then multiply working days minus days off
adjusted_salary = salary_per_hour * hours_per_day * (working_days - holidays_per_year - vacation_per_year)

print('=' * DASH_LINE)  # separation line
print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: ${annual_salary:6,.2f}")  # prints annual salary for user
print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: ${adjusted_salary:6,.2f}")  # prints adjusted salary

print('=' * DASH_LINE)  # separation line
print("Goodbye!")  # says goodbye to the user
