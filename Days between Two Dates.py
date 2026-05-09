from datetime import date
from datetime import datetime

date1 = input()
date2 = input()

D1 = datetime.strptime(date1,"%Y-%m-%d")
D2 =  datetime.strptime(date2,"%Y-%m-%d")

days = (D2 - D1).days

print(days)
