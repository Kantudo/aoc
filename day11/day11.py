#!/usr/bin/env python3


rows = []
with open('./day11_input.txt') as file:
    line = file.readline().replace('\n', '')
    while line:
        rows.append(line)
        line = file.readline().replace('\n', '')

def count_adj(rows, i, j, c, part):
    count = 0
    if part == 1:
        posj = [j-1, j, j+1]
        posi = [i-1, i, i+1]
        for idi in posi:
            for idj in posj:
                try:
                    if idj < 0 or idi < 0: raise
                    count = count + rows[idi][idj].count(c)
                except Exception as e:
                    pass
        count = count - rows[i][j].count(c)

        return count
    else:
        posj = [-1, 0, +1]
        posi = [-1, 0, +1]
        for idi in posi:
            for idj in posj:
                try:
                    ni = i+idi
                    nj = j+idj
                    while rows[ni][nj] == '.':
                        ni = ni + idi
                        nj = nj + idj
                    #    if idi == 0 and idj == 0: raise
                    if ni < 0 or nj < 0: raise
                    #print(rows[ni][nj])
                    count = count + rows[ni][nj].count(c)
                except Exception as e:
                    pass
        count = count - rows[i][j].count(c)
        return count

def iter_rows(rows, part):
    if part == 1: mon_max = 4
    else: mon_max = 5
    rows_aux = []
    changed = False
    for i, row in enumerate(rows):
        row_aux = ''
        for j, seat in enumerate(row):
            if seat == 'L':
                adj = count_adj(rows, i, j, '#', part)
                if adj == 0:
                    row_aux = row_aux + '#'
                    changed = True
                else:
                    row_aux = row_aux + seat
            elif seat == '#':
                adj = count_adj(rows, i, j, '#', part)
                if adj >= mon_max:
                    row_aux = row_aux + 'L'
                    changed = True
                else:
                    row_aux = row_aux + seat
            else:
                row_aux = row_aux + seat
        rows_aux.append(row_aux)
    return changed, rows_aux

aux_rows = rows

changed = True
while changed:
    changed, rows = iter_rows(rows, 1)

occ = 0
for row in rows:
    occ = occ + row.count('#')

print(occ)

##### Part 2

rows = aux_rows

changed = True
while changed:
    changed, rows = iter_rows(rows, 2)

occ = 0
for row in rows:
    occ = occ + row.count('#')

print(occ)
