import re
import sys


def getConsultInfo(days: int):
    time = []
    income = []
    for i in range(days):
        info = sys.stdin.readline().split()
        income.append(info.pop())
        time.append(info.pop())
    return time, income


def isAvailable(day, time):
    if (day > len(time) or (day + int(time[day - 1])) > (len(time) + 1)):
        return False
    else:
        return True


def getConsultDays(days: int, time):
    consultDays = []
    for _ in range(days):
        i = 1
        while (isAvailable(i, time)):
            index = []
            index.append(int(i))
            i += int(time[i - 1])
        consultDays.append(index)

    return consultDays


daysLeft = int(sys.stdin.readline())
consultTime, income = getConsultInfo(daysLeft)
print(getConsultDays(daysLeft, consultTime))


def getMaximumIncome():
    case, income = getConsultDays()
    for i in range(len(case)):
        each = case[i]
        total = 0
        for j in each:
            total += int(income[j - 1])
        case[i] = total
        if (i > 0):
            if (int(case[i - 1]) <= case[i]):
                maxIncome = case[i]
    return maxIncome

# print(getMaximumIncome())
