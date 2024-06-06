# If a year is evenly divisible by 4, 100, and 400, then it is a leap year
year=int(input('year:'))
if (year%4==0):
    if (year % 100==0):
        if (year%400==0):
            print("leap year",year)
        else:
            print("not a leap year",year) 
    else:
         print(f"leap year{year}")              
else:
    print("not leap year",year)         