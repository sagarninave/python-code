from datetime import date, time, datetime, timedelta

print('\n')
print("time span ", timedelta(days=365, hours=5, minutes=1))

print('\n')
today = date.today()
print("today's date : ", today)
print("1 year after date without time", today + timedelta(days=365))
print("after 2 weeks and 5 day :", today + timedelta(days=5, weeks=2))

print('\n')
datetime = datetime.now()
print("today's date time : ", datetime)
print("1 year after date with time", datetime + timedelta(days=365))

print('\n')
week = datetime - timedelta(weeks=1, days=3)
last_week = week.strftime("%A %d %B %Y")
print("Date of last week : ",last_week)
