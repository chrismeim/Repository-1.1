month_days = {"January":31, "February": 28,"March": 31, "April": 30, "May": 31, "June":30, "July":31, "August":31, "September":30, "October": 31, "November":30, "December":31}
month = input("What is the month you want to know? ")  
if  month == "February":
    print(f"February has {month_days[key]} or 29 days ")
else:
    print(f"{month} has {month_days[key]} days")