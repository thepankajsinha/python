import datetime

now = datetime.datetime.now()
print("Current date and time:", now) #2025-07-10 20:05:31.962922
print("Year:", now.year) #2025
print("Month:", now.month) #7
print("Day:", now.day) #10
print("Hour:", now.hour) #20
print("Minute:", now.minute) #5
print("Second:", now.second) #31
print("Microsecond:", now.microsecond) #962922





# Formatting the date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date) #Formatted date: 2025-07-10 20:05:31