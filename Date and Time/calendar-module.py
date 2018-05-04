from datetime import date
import calendar

month, day, year = map(int, input().split())

input_date = date(year, month, day)
print(calendar.day_name[input_date.weekday()].upper())
