
# Program to check whether a year is a leap year

year = int(input("Enter a year: "))

# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

