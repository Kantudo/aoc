import numpy as np

jolts = []
with open('day10_input.txt') as file:
    line = file.readline().replace('\n', '')

    while line:
        jolts.append(int(line))
        line = file.readline().replace('\n', '')
jolts.append(max(jolts)+3)
jolts.append(0)
jolts.sort()
diffs = np.subtract(jolts[1:], jolts[:-1])
diffs = diffs.tolist()
sol1 = diffs.count(1)*diffs.count(3)
print(sol1)

######

def valid(num):
    if num < 3:
        res = 2**num
    elif num == 3:
        res = 7
    else:
        res = (2**(num-3))*7
    return res

diffs = np.subtract(jolts[2:], jolts[:-2])
diffs = diffs.tolist()

n = 0
idx = 0
aux = []
while idx < len(diffs):
    d = diffs[idx]
    if d == 2:
        n = n+1            
    else:
        if n > 0: aux.append(n)
        n = 0
    idx = idx + 1

total = 1
for el in aux:
    total = total*valid(el)

print(total)