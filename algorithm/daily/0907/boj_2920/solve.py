import sys
sys.stdin = open('input.txt')
nums = [*map(int,input().split())]
sort_nums = range(1,9)
r_sort_nums = range(8,0,-1)

def check():
    for i in range(8):
        if nums[i] != sort_nums[i]: break
    else: print('ascending');return 0

    for i in range(8):
        if nums[i] != r_sort_nums[i]: break
    else: print('descending'); return 0

    print('mixed'); return 0

check()