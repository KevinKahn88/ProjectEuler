'''
Created on Sep 15, 2015

@author: Kevin
'''

def leapyear(num):
    return (num%4 == 0) & ((num%100!=0) | (num%400==0))

if __name__ == '__main__':
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayTrack = 1
    sunTrack = 0
    
    dayTrack = (dayTrack+sum(monthDays))%7
    year = 1901;

    while year < 2001:
        print(dayTrack)
        for ind in range(12):
            if not dayTrack:
                sunTrack+=1
            dayTrack += monthDays[ind]
            if (ind == 1) & leapyear(year):
                dayTrack += 1
            dayTrack = dayTrack%7
        year +=1
    print(sunTrack)