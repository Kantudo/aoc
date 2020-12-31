
lines = []

with open('day14_input.txt') as file:

    line = file.readline().replace('\n', '')

    while line:
        lines.append( line )
        line = file.readline().replace('\n', '')

def sum_mem(mem):
    s = 0
    for key in mem:
        s += mem[key]
    return s

mask = 1
mem = {}
for inst in lines:
    if 'mask' in inst:
        exec(inst)

        mask0 = int(mask.replace('X', '1'), 2)
        mask1 = int(mask.replace('X', '0'), 2)
    else:
        num = int(inst[inst.index('=') + 2:])
        num = (num & mask0) | mask1
        pos = inst[inst.index('[')+1:inst.index(']')]
        
        mem[pos] = num


print(sum_mem(mem))

####

def enum_pos(mask, address):
    pos_list = []
    numX = mask.count('X')
    address_formated = f'{{0:0{str(len(mask))}b}}'.format(address)
    for n in range(0, 2**numX):
        num = f'{{0:0{ numX }b}}'.format(n)
        pos = ''
        for i, char in enumerate( address_formated ):
            if mask[i] == 'X':
                pos += num[0]
                num = num[1:]
            else:
                if mask[i] == '0': pos += char
                else: pos += mask[i]
        pos_list.append(pos)
    return pos_list
    
mem = {}
for inst in lines:
    if 'mask' in inst:
        exec(inst)
    else:
        num = int(inst[inst.index('=') + 2:])
        address = int( inst[inst.index('[')+1:inst.index(']')] )

        pos_list = enum_pos(mask, address)
        #[ print(pos) for pos in pos_list]
        for pos in pos_list:
            mem[pos] = num

print(sum_mem(mem))

