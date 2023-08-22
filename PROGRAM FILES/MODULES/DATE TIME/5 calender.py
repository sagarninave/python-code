import calendar

print('\n\t\t\t plain text calendar\n')
plain_text_calendar = calendar.TextCalendar(calendar.SUNDAY)
final_plain_text_calendar = plain_text_calendar.formatmonth(2019,2,0,0)
print(final_plain_text_calendar)

print('\n\t\t\t HTMLMcalendar \n')
html_calendar = calendar.HTMLCalendar(calendar.SUNDAY)
final_html_calendar = html_calendar.formatmonth(2019,2)
print(final_html_calendar)

for month_days in plain_text_calendar.itermonthdays(2019, 6):
    print(month_days)
    
for month_name in calendar.month_name:
    print(month_name)
    
print('\n')

for day_name in calendar.day_name:
    print(day_name)

for m in range(1, 13):
    cal = calendar.monthcalendar(2019, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))
