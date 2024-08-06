#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Lia Brown
Semester: Summer - 2024
Description: <fill this in>
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...
    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year

    return leap_flag

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day
    

    
    if day > mon_max(mon, year):
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    '''
    Before() -> date for previous day in DD/MM/YYYY string format

    Return the date for the previous day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''

    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  #previouss day



    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_max(mon, year) if mon != 2 or not leap_year(year) else 29

    return f"{day:02}/{mon:02}/{year}"
def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...
    #check if the date lenght is 10 characters 2 for month 2 for day and 4 for year.
    if len(date) != 10:
        return False
    
    #extract components and converts to integers
    day = int(date[:2])
    mon = int(date[3:5])
    year = int(date[6:])

    
    #check if the month is valid
    if mon < 1 or mon > 12:
        return False
    
    #check if the day is valid for the month and year
    if day < 1 or day > mon_max(mon, year):
        return False
    
    return True


def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    ...
    #initialize the date variable woth start date
    date = start_date
    if num >= 0:
        while num > 0:
            date = after(date)
            num -= 1
    else:
        while num < 0:
            date = before(date)
            num += 1
    return date

if __name__ == "__main__":
# check length of arguments
    if len(sys.argv) != 3:
        usage() #call the usage function if the number of arguement is not 3
    
    # check first arg is a valid date
    start_date = sys.argv[1]
    is_correct_date = valid_date(start_date) #i validate the start date format from valid_date function
    #i call the usage function to pringt usage instruction and exit the srart date if is invalid
    if is_correct_date == False:
        usage()

    # check that second arg is a valid number (+/-)
    num_str = sys.argv[2]
    valid_number = True #check to assume that number is accurate first
    

    #check if the number is negative
    if num_str[0] == '-':
        num_str_body = num_str[1:]  #check to get the part after the minus sign
    else:
        num_str_body = num_str #if the number is postive, use it as is
    
    if num_str_body == '':  #check if the body is empty
        valid_number = False
    else:
        #check each char in the body if its a digit
        for char in num_str_body:
            if char < '0' or char > '9':
                valid_number = False
                break #stop cheching if find a non digit char
    
    if valid_number == False: #if number is not valid, its show usage instruction and exit
        usage()
    #convert valid number string to integer
    num_days = int(num_str)

    # call day_iter function to get end date, save to x
    x = day_iter(start_date, num_days)
    
    # print(f'The end date is {day_of_week(x)}, {x}.')
    print(f'The end date is {day_of_week(x)}, {x}.')

    pass