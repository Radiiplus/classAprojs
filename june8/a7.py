import calendar

year = int(input("Enter year: "))
month = input("Enter month (name or number): ")

if month.isdigit():
    m = int(month)
else:
    m = list(calendar.month_name).index(month.capitalize())

print(calendar.month(year, m))