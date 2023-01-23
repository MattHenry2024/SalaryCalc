DASH_LINE = 40  #this is a variable for separation lines

print('=' * DASH_LINE)  #separation line
print("The Salary Calculator Program")  #welcome the user
print('=' * DASH_LINE)  #separation line

COLUMN_LENGTH = 25

salary_per_hour = float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: "))
hours_per_week = float(input(f"{'Hours per week':.<{COLUMN_LENGTH}}: "))
days_per_week = float(input(f"{'Days per week':.<{COLUMN_LENGTH}}: "))
holidays_per_year = float(input(f"{'Holidays per year':.<{COLUMN_LENGTH}}: "))
vacation_per_year = float(input(f"{'Vacation days per year':.<{COLUMN_LENGTH}}: "))

working_days = days_per_week * 52
hours_per_day = hours_per_week / days_per_week

annual_salary = salary_per_hour * hours_per_day * working_days
adjusted_salary = salary_per_hour * hours_per_day * (working_days - holidays_per_year - vacation_per_year)

print('=' * DASH_LINE)
print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: ${annual_salary:6,.2f}")
print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: ${adjusted_salary:6,.2f}")

print('=' * DASH_LINE)
print("Goodbye!")