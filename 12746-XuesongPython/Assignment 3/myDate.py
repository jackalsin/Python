class myDate:

    def __init__(self, y, m, d):
        # Task 2.a. Complete this method and check whether the values for year, month and date
        # are valid or not. For example, there should not be more than 30 days in April.
        if self.checkMonthDate(y, m, d):
            self.year = y
            self.month = m
            self.date = d
        else:
            raise Exception("Not valid input year = ", y, " month = ", m, " date = ", d)

        # Check if this is a valid year, month and date input.
        # ref: https://en.wikipedia.org/wiki/Leap_year
    def checkMonthDate(self, y, m, d):
        if self.isLeapYearHelper(y):
            febDays = 29
        else:
            febDays = 28
        monthToDate = {1: 31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31, 2:febDays}
        if m <= 0 or m > 12: return False
        if d <= 0 or d > monthToDate[m]: return False
        return True

    def isLeapYearHelper(self, y):
        if y % 4 != 0:
            return False
        elif y % 100 != 0:
            return True
        elif y % 400 != 0:
            return False
        else:
            return True

    # Task 2.b.
    def isLeapYear (self): # return 1 if the year of the date is leap year
        return 1 if self.isLeapYearHelper(self.year) else 0

    # Task 2.b.
    def DaysinMon (self): #return the number of days in that month, you need to consider leap year here
        return self.daysinMonHelper(self.year)

    def daysinMonHelper(self, year):
        return self.__daysInMonth(self.month)

    def __daysInMonth(self, month):
        if self.isLeapYearHelper(self.year):
            febDays = 29
        else:
            febDays = 28
        monthToDate = {1: 31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31, 2:febDays}
        return monthToDate[month]

    # Task 2.b.
    #  Implement the == function in myDate()
    def __eq__(self, other):
        return type(other) == type(self) and self.year == other.year \
               and self.month == other.month and self.date == other.date

    # Task 2.b.
    # Implement comparison between two myDate type, this is used to sort an array of Dates in Sorted()
    def __cmp__(self, other):
        # return any negative integer if "self" is earlier than "other", zero if self == other,
        #  return a positive number if "self" is later than "other"
        if type(other) == type(self):
            thisNum = int(self.year) * 1000 + int(self.month) * 10 + int(self.date)
            otherNum = int(other.year) * 1000 + int(other.month) * 10 + int(other.date)
            return thisNum - otherNum
        raise Exception("Wrong type other: " + str(type(other)))

    # Implement subtraction between two myDate type, you may need to use the functions defined above
    def __sub__(self, other):
        # return the number of days between two myDate class, negative if "self" is earlier than "other", zero if self == other, positive if "self" is later than "other"
        if self.__cmp__(other) < 0:
            minDate, maxDate, sign = self, other, -1
        else:
            minDate, maxDate, sign = other, self, 1
        days = 0
        if (type(other) == type(self)):
            for year in xrange(minDate.year, maxDate.year):
                if self.isLeapYearHelper(year):
                    days += 366
                else:
                    days += 365
            for monthChild in xrange(1, maxDate.month):
                days += maxDate.__daysInMonth(monthChild)
            for monthChild in xrange(1, minDate.month):
                days -= maxDate.__daysInMonth(monthChild)
            return (days + maxDate.date - minDate.date) * sign

        raise Exception("Wrong type other: " + type(other))

    # Implement the print method for myDate
    def __repr__(self):
        return str(self.year) + " " + str(self.month) + " " + str(self.date)

# Verify you class here

date1 = myDate(2015, 9, 1)
print (date1)
date2 = myDate(2010, 4, 25)
date3 = myDate(2014, 8, 8)
print ( date2 == date3)
print ( date1 - date2 )
print ( date2 - date3 )
sorted([date1,date2,date3])
print sorted([date1,date2,date3])


date4 = myDate(2015, 2, 29)
