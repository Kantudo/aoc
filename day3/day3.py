#!/usr/bin/env python
xpos = 0
trees = 0

with open('day3_input.txt') as file:
    mon = file.readline()
    while mon:
        if mon[xpos] == '#':
            trees = trees + 1

        mon = file.readline()

        xpos = xpos + 3
        xpos = xpos % (len(mon)-1)
print(trees)

down = [1, 1, 1, 1, 2]
right = [1, 3, 5, 7, 1]
i = 0
total = 1;
for dis in right:
        trees = 0
        with open('day3_input.txt') as file:
                mon = file.readline()
                while mon:
                        if mon[xpos] == '#':
                                trees = trees + 1
                                mon = mon[:xpos] + 'O' + mon[xpos:]
                        for j in range(0, down[i]):
                                mon = file.readline()
                        print(mon.replace('\n', ''))
                        xpos = xpos + dis
                        xpos = xpos % (len(mon)-1)
        total = total*trees
        i = i+1

print(total)
