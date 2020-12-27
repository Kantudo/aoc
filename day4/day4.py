#!/usr/bin/env python

def get_fields(line):
    line = line.split(' ')
    arr = [el[0:el.find(':')] for el in line]
    return arr

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0
with open('day4_input.txt') as file:
    line = file.readline()
    while line:
        # print(line)
        arr = []
        while len(line) > 1:
            arr = arr + get_fields(line)
            line = file.readline()
        if 'cid' in arr:
            arr.remove('cid')
        if len(arr) == 7:
            valid = valid + 1
        line = file.readline()

print(valid)

##2

def get_fields(line):
    line = line.replace('\n', '').split(' ')
    arr = {el[0:el.find(':')]:el[el.find(':')+1:] for el in line}
    return arr

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecolor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid = 0
with open('day4_input.txt') as file:
    line = file.readline()
    while line:
        # print(line)
        arr = {}
        while len(line) > 1:
            arr = arr | get_fields(line)
            line = file.readline()
        if 'cid' in arr:
            arr.pop('cid')
        mon_sum = 0
        if len(arr) == 7:
            # print(arr)
            # input()
            mon_sum = 1
            if int(arr['byr']) >= 1920 and int(arr['byr']) <= 2002:
                pass
            else:
                mon_sum = 0
            if int(arr['iyr']) >= 2010 and int(arr['iyr']) <= 2020:
                pass
            else:
                mon_sum = 0

            if int(arr['eyr']) >= 2020 and int(arr['eyr']) <= 2030:
                pass
            else:
                mon_sum = 0

            if len(arr['hgt']) > 2:
                if arr['hgt'][-2:] == 'cm':
                        if int(arr['hgt'][:-2]) >= 150 and int(arr['hgt'][:-2]) <= 193:
                            pass
                        else:
                            mon_sum = 0
                else:
                        if int(arr['hgt'][:-2]) >= 59 and int(arr['hgt'][:-2]) <= 76:
                            pass
                        else:
                            mon_sum = 0
            else:
                mon_sum = 0

            if arr['hcl'][0] == '#' and len(arr['hcl']) == 7:
                pass
            else:
                mon_sum = 0

            if arr['ecl'] in eyecolor:
                pass
            else:
                mon_sum = 0

            if len(arr['pid']) == 9:
                pass
            else:
                mon_sum = 0

        valid = valid + mon_sum
        # mon_sum = 0
        line = file.readline()

print(valid)
