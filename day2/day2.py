#!/usr/bin/env python

faulty = 0

with open('day2_input.txt') as file:
    mon = file.readline()
    while mon:
        low = int(mon[0:mon.find('-')])
        high = int(mon[mon.find('-')+1:mon.find(' ')])
        char = mon[mon.find(' ') + 1]
        pas = mon[mon.find(' ') + 4:]
        print(mon.replace('\n', ''))
        # print(low)
        # print(high)
        occur = pas.count(char)
        print(char)
        # print(pas)
        if (occur > high)  or (occur < low):
            faulty = faulty + 1;
            # print(mon)
            # print(occur)
        mon = file.readline()


# print(mon.find(' '))
print(faulty)

correct = 0
with open('day2_input.txt') as file:
    mon = file.readline()
    while mon:
        low = int(mon[0:mon.find('-')])
        high = int(mon[mon.find('-')+1:mon.find(' ')])
        char = mon[mon.find(' ') + 1]
        pas = mon[mon.find(' ') + 4:]
        print(mon.replace('\n', ''))
        pas = pas[low-1] + pas[high-1]
        occur = pas.count(char)
        print(char)
        # print(pas)
        if (occur == 1):
            correct = correct + 1;
            # print(mon)
            # print(occur)
        mon = file.readline()
print(correct)
