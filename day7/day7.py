#!/usr/bin/env python
bag_dict = {}
target = 'shiny gold'

def check_shiny(key):
    res = False
    if key in bag_dict and target in bag_dict[key]:
        return True
    elif key in bag_dict:
        for bag in bag_dict[key]:
            res = res or check_shiny(bag)
    else:
         return False

    return res


with open('day7_input.txt') as mon_file:
    line = mon_file.readline().replace('\n', '')
    while line:
        bag = line[0:line.index('bags')-1]
        aux = line[line.index('contain') + len('contain') + 1:]
        aux = aux.split(', ')
        contains = [bag[2:bag.index('bag')-1] for bag in aux]
        if not 'no other' in line:
            bag_dict[bag] = contains
        # print(bag)
        # print(contains)
        # input()

        line = mon_file.readline()
# print(bag_dict)
total = 0
for key in bag_dict:
    if check_shiny(key):
        total = total + 1
print(total)


bag_dict = {}

def count_nested(key):
    if not bag_dict[key]:
        return 0
    else:
        total_bags = 0
        for bags in bag_dict[key]:
            total_bags = total_bags + bags[0] + bags[0]*count_nested(bags[1])
        return total_bags

with open('day7_input.txt') as mon_file:
    line = mon_file.readline().replace('\n', '')
    while line:
        bag = line[0:line.index('bags')-1]
        aux = line[line.index('contain') + len('contain') + 1:]
        aux = aux.split(', ')
        if not 'no other' in line:
            contains = [[int(bag[0]), bag[2:bag.index('bag')-1]] for bag in aux]
        else:
            contains = False
        bag_dict[bag] = contains
        # print(bag)
        # print(contains)
        # print(bag_dict)
        # input()

        line = mon_file.readline()
print(count_nested('shiny gold'))
