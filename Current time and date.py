from datetime import date , time, datetime
#calling the today
#function of date class 
today = date.today()
now = datetime.now()
print("Today is the", today)
print("\nCurrent date and time are", now)
#printing date's components
print("\nDate Components", today.year, today.month, today.day)