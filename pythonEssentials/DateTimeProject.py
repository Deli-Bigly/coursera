"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):

    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    date1 = datetime.date(year, month, 1)
    #print("Date we are referencing: ", date1)

    #or method works okay for adding one month, unless that month is december
    if date1.month <= 11:
        date2 = datetime.date(year, month+1, 1)
        difference = date2 - date1
        #print ("This month has: ", difference, " Days")

    else: #if the month is december
        date2 = datetime.date(year+1, month-11, 1)
        difference = date2 - date1
        #print ("This month has: ", difference, " Days")

    #Read time delta attribute "days" to a variable
    #difference_days = difference.days
    #returns the number of days in the provided month
    return difference.days

def is_valid_date(year, month, day):

    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """

    #First check if the year is valid or not
    if (year >= datetime.MINYEAR and year <= datetime.MAXYEAR):
        year_check = True
        #print("Year Check: \t", year_check)
    else:
        year_check = False
        return False
        #print("Year Check: \t", year_check)


    #Then check if the month is valid or not
    if (month >= 1 and month <= 12):
        month_check = True
        #print("Month Check: \t", month_check)
    else: 
        month_check = False
        return False
        #print("Month Check: \t", month_check)


    #Then check if the number of days of the specified month are within the limits of that month
    days_in_month_v = days_in_month(year, month)
    if (day >= 1 and day <= days_in_month_v):
        day_check = True
        #print("Day Check: \t", day_check)
    else: 
        day_check = False
        return False
        #print("Day Check: \t", day_check)


    #finally we check all three values for True/False to determin return value
    if (year_check == 1 and month_check == 1 and day_check == 1):
        return True
    else:
        print("The date is not valid")
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        pass
    else:
        print("Invalid Dates")
        return 0

    #convert dates to use our date class imported from datetime
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    #subtract the two dates to get the difference
    time_delta = date2 - date1

    if time_delta.days <= 0:
        print("The second date is before or equal to the first date")
        return 0
    else:
        return time_delta.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """

    #Get todays date
    today = datetime.date.today()

    #Check if entered birthday is valid
    if is_valid_date(year, month, day):
        pass
    else: 
        return 0
    
    #Check the time delta between the two dates
    time_delta = days_between(year, month, day, today.year, today.month, today.day)

    #returns the difference in days
    return time_delta

#print("Your age in Days is: ", age_in_days(1999, 11, 12))
