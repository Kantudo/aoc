lines = []
with open('day8_input.txt') as file:
    line = (file.readline()).replace('\n', '')
    while line:
        lines.append(line)
        line = (file.readline()).replace('\n', '')
# print(lines)
acc = 0
executed = []
idx = 0
while True:
    inst = (lines[idx])[0:lines[idx].index(' ')]
    num = int((lines[idx])[lines[idx].index(' ') + 1:])
    if not idx in executed: executed.append(idx)
    else: break

    if inst == 'acc':
        acc = acc + num
        idx = idx + 1
    elif inst == 'jmp':
        idx = idx + num
    elif inst == 'nop':
        idx = idx + 1
print(acc)


#####

poss = ['jmp', 'nop']
for i, el in enumerate(lines):
    mon_inst = el[0:el.index(' ')]
    num = el[el.index(' ') + 1:]

    if mon_inst in poss:
        lines[i] = poss[(poss.index(mon_inst) + 1) % 2] + ' ' + num
    acc = 0
    idx = 0
    executed = []
    while True:
        inst = (lines[idx])[0:lines[idx].index(' ')]
        num = int((lines[idx])[lines[idx].index(' ') + 1:])
        if not idx in executed: executed.append(idx)
        else: break

        if inst == 'acc':
            acc = acc + num
            idx = idx + 1
        elif inst == 'jmp':
            idx = idx + num
        elif inst == 'nop':
            idx = idx + 1
        if idx >= len(lines): break
    
    if mon_inst in poss:
        lines[i] = el
        if idx >= len(lines):
            print(i)
            break

print(acc)