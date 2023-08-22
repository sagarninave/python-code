from datetime import date, datetime

date = date.today()
print('\n')
print("today's date is: ", date)

print('\n')

print("today is: ", date.day, date.month, date.year)

print('\n')

print("today's weekday number is: ", date.weekday())

print('\n')

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THUSDAY', 'FRIDAY', 'SATURDAY']

print("todays weekday is: ", days[date.weekday()])

print('\n')

print("todayts date and time now is: ", datetime.now())

print('\n')

print("todays time from datetime is: ", datetime.time(datetime.now()))
