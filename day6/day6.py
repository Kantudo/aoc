#!/usr/bin/env python

with open('day6_input.txt') as file:

    line = file.readline()

    total = 0
    while line:
        arr = []
        while len(line) > 1:
            arr = arr + [c for c in line.replace('\n', '') if not c in arr]
            line = file.readline()
        # print(arr)
        # input()
        total = total + len(arr)
        line = file.readline()
print(total)


with open('day6_input.txt') as file:

    line = file.readline()
    # people = 1

    total = 0
    while line:
        arr = []
        arr_aux = []
        people = 0
        while len(line) > 1:
            arr = arr + [c for c in line.replace('\n', '') if not c in arr]
            arr_aux = arr_aux + [c for c in line.replace('\n', '')]
            people = people + 1
            line = file.readline()
        arr_aux.sort()
        answered = [arr_aux.count(q) for q in arr]
        total = total + answered.count(people)

        line = file.readline()
print(total)
