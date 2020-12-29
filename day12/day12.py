#!/usr/bin/env python3

moves = []
with open('day12_input.txt') as file:
    line = file.readline().replace('\n', '')

    while line:
        moves.append(line)
        line = file.readline().replace('\n', '')
dirs = {'N':[0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
dirs_list = ['N', 'E', 'S', 'W']
facing = 'E'
pos = [0, 0]
for el in moves:
    num = int(el[1:])
    code = el[0]
    if code in dirs_list:
        for i, val in enumerate(pos):
            pos[i] =  val + dirs[code][i]*num
    elif code == 'F':
        for i, val in enumerate(pos):
            pos[i] =  val + dirs[facing][i]*num
    else:
        if code == 'R': facing = dirs_list[(dirs_list.index(facing) + int(num/90)) % 4]
        else: facing = dirs_list[(dirs_list.index(facing) - int(num/90)) % 4]
print( abs(pos[0]) + abs(pos[1]) )

###

def sign(n):
    return n/abs(n)

dirs = {'N':[0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
dirs_list = ['N', 'E', 'S', 'W']
facing = 'E'
pos = [0, 0]
wayp = [10, 1]
for el in moves:
    num = int(el[1:])
    code = el[0]
    if code in dirs_list:
        for i, val in enumerate(wayp):
            wayp[i] =  val + dirs[code][i]*num
    elif code == 'F':
        for i, val in enumerate(pos):
            pos[i] =  val + wayp[i]*num
    else:
        if code == 'L':
            for i in range(0, int(num/90)):
                aux = wayp[0]
                wayp[0] = wayp[1] * -1
                wayp[1] = aux
        else:
            for i in range(0, int(num/90)):
                aux = wayp[0]
                wayp[0] = wayp[1]
                wayp[1] = aux * -1
    # print('pos ' + str(pos))
    # print('wayp ' + str(wayp))
    # input()
print( abs(pos[0]) + abs(pos[1]) )