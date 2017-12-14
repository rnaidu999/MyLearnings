

from datetime import datetime
from datetime import date

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


#dat1=input("Enter Start Date :")
#dat2=input("Enter End Date :")
#print(days_between(dat1,dat2))

d1=date(2014,1,1)
d2=date(2014,1,15)
delta=d2-d1
print(delta.days)

val=['',2,2,'']
val2=[]
val2=[var for var in val if var]
print(val2)

list11=[2,2,3,3,4,4]
list11.remove(2)
print(list11)


#get today time and year
import calendar
from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

print (currentHour, currentMinute, currentSecond, currentYear, currentMonth, currentDay)
cal=calendar.TextCalendar()
print (cal.prmonth(currentYear,currentMonth))
