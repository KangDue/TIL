import sys
sys.stdin = open('input.txt')
"""
첫째 줄: 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)
둘째 줄: 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄: M(1 ≤ M ≤ 500,000)
넷째 줄: 상근이가 몇개 가진지 파악 해야할 카드에 적힌 수 M개
"""
info = dict()
n,nums,m,finds = open('input.txt')
nums = [*map(int,nums.split())]
finds = [*map(int,finds.split())]
for i in nums:
    if info.get(i): info[i] += 1
    else: info[i] = 1
print(*map(lambda x:info.get(x,0), finds))

