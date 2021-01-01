from collections import deque
mon_nums = [2,15,0,9,1,20]

def nth_num(nums, nth):
    checked = []
    index = {}
    num = 0
    for i, num in enumerate(nums): 
        index[num] = [i+1, i+1]
    for turn in range(len(nums)+1, nth + 1):
        diff = index[num][0] - index[num][1]
        if diff:
            num = diff
            try:
                index[num][1] = index[num][0]
                index[num][0] = turn
            except:
                index[num] = [turn, turn]
        else:
            num = 0
            try:
                index[num][1] = index[num][0]
                index[num][0] = turn
            except:
                index[num] = [turn, turn]
        #print(num)
    return num
print(nth_num(mon_nums, 2020))
###
print(nth_num(mon_nums, 30000000    ))
