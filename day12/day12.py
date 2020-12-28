#!/usr/bin/env python3

dirs = []
with open('day12_input.txt') as file:
    line = file.readline().replace('\n', '')

    while line:
        dirs.append(line)
        line = file.readline().replace('\n', '')
