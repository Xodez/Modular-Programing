#   Name; slicing
#   Desc: details of slicing
#   Author: Helen Fagan
days = [ "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
midweek= days[1:4]
print(midweek)
firstThreeDays = days[:3]
print(firstThreeDays)

lastDay = days[-1]
print(lastDay)
secondLastDay = days[-2]
print(secondLastDay)
firstThreeDays = days[-7:-4]    # indices -7, -6. -5
print(firstThreeDays)

lastThreeDays = days[-3:]   # start at -3 until end of the list
print(lastThreeDays)

all = days[:]
print(all)

endDays = days[5:19] # runs from 5 to 6 (could go to 19 but there is not 19)
print(endDays)

# days[19] = "Not a day"

everySecondDay = days[0:7:2]
print(everySecondDay)
empty = days[2:1]
print(empty)

