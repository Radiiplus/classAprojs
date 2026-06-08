import calendar

year = int(input("Enter year: "))

start = input("Enter start month (name or number): ")
end = input("Enter end month (name or number): ")

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

if start.isdigit():
    start_m = int(start)
else:
    start_m = months.index(start.capitalize()) + 1

if end.isdigit():
    end_m = int(end)
else:
    end_m = months.index(end.capitalize()) + 1

for m in range(start_m, end_m + 1):
    print(calendar.month(year, m))