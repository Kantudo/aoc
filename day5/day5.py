#!/usr/bin/env python

def decode(a):
    if a[0] == 'F' or a[0] == 'L':
        num = 0
    else:
        num = 2**(len(a)-1)

    if len(a) == 1:
        return num
    else:
        num = num + decode(a[1:])
    return num
id = []
with open('day5_input.txt') as file:
    line = file.readline().replace('\n', '')

    curr_max = decode(line[0:7])*8 + decode(line[7::])
    # print(line)
    # print(line[0:7])
    # print(line[7::])
    # input()

    while line:
        now_max = decode(line[0:7])*8 + decode(line[7::])
        if now_max > curr_max:
            curr_max = now_max
        line = file.readline().replace('\n', '')
print(curr_max)

import numpy as np

ids = []
with open('day5_input.txt') as file:
    line = file.readline().replace('\n', '')

    mon_id = decode(line[0:7])*8 + decode(line[7::])
    ids.append(mon_id)
    while line:
        mon_id = decode(line[0:7])*8 + decode(line[7::])
        ids.append(mon_id)
        line = file.readline().replace('\n', '')
ids.sort()

diff = np.subtract(ids[:-1], ids[1::])
# diff.tolist()
i = 95
while i<838:
    if not(i in ids):
        print(i)
    i = i+1
print(diff)
# print(ids[diff.tolist().index(0)])
