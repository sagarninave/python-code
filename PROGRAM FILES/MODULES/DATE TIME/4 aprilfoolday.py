from datetime import date, time, datetime, timedelta


print('\n')

today = date.today()
print("today's date is: ", today)

afd = date(today.year, 4, 1)
print("April fool day: ", afd)

if afd < today:
    print("april fool day has gone %d day before: " %((today - afd).days))
    afd = afd.replace(year = today.year+1)

next_year_afd = afd-today
print("next year afd is after", next_year_afd.days, "days")
