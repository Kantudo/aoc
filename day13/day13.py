from math import ceil, floor, prod

with open('day13_input.txt') as file:

    start = int(file.readline().replace('\n', ''))
    buses = file.readline().replace('\n', '')


ids = [ int(el) for el in buses.split(',') if not el == 'x' ]
times = [ ceil(start/bus_id)*bus_id for bus_id in ids]

sol1 = ( times[times.index(min(times))] - start ) * ids[times.index(min(times))]
print(sol1)

#####

off = [ buses.split(',').index(str(bus_id)) for bus_id in ids ]
idmax = max(ids)
idmax_index = ids.index(idmax)
t = 1
i = 0
inc = 1
while True:
    if (t + off[i]) % ids[i] == 0:

        inc = inc*ids[i]
        i = i + 1
        if i == len(ids): break
    t = t+inc
print(t)
