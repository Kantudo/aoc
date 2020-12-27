nums = []
with open('day9_input.txt') as file:
    line = file.readline().replace('\n', '')

    while line:
        nums.append(int(line))
        line = file.readline().replace('\n', '')
#print(len(nums))
idx = 25
#print(nums[idx])
while True:
    good = False
    for j in range(0, 25):
        for k in range(0, 25):
            #print(nums[k+idx-25] + nums[j+idx-25])
            if (nums[k+idx-25] + nums[j+idx-25] == nums[idx]):# and (j != idx) and (k != idx):
                good = True
                break
        
    if good:
        idx = idx + 1
    else:
        break
    if 24 + idx >= len(nums): break
print(nums[idx])
key = nums[idx]


idx = 0
first = idx
total = 0
while True:
    total = total + nums[idx + first]
    if total >= key:
        if total == key:
            weakness = min(nums[first:idx + first+1]) + max(nums[first:idx + first+1])
            break
        else:
            first = first + 1
            idx = 0
            total = 0
    else:
        idx = idx + 1
    

print(weakness)
