def is_leap(year):
    leap = year
    if leap%400==0:
        return True
    elif leap%100==0:
        return False
    elif leap%4==0:
        return True
    else:
        return False

year = int(input())
