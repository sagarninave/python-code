from datetime import date, time, datetime

print('\n')

now = datetime.now()

print('\n')
print(now)
print(now.strftime("the current date : %d %b"))

print('\n')

print(now.strftime("the current year with last two digit by small y: %y"))
print(now.strftime("the current year with last four digit by capital Y: %Y"))

print('\n')

print(now.strftime("the current weekday with three letters : %a"))
print(now.strftime("the current weekday with full length letter : %A"))

print('\n')

print(now.strftime("the current month with three letters : %b"))
print(now.strftime("the current month with full length letter : %B"))

print('\n')
print("############ DATE FORMATTING #############")
print(now.strftime("today's day dand current day : %a %d %B %y"))

print('\n')

print(now.strftime("the local date and time : %c"))
print(now.strftime("local date : %x"))
print(now.strftime("local time : %X"))

print('\n')
print("############ TIME FORMATTING #############")
print(now.strftime("current time for 12 hours: %I:%M:%S %p"))
print(now.strftime("current time for 24 hours: %H:%M %p"))
