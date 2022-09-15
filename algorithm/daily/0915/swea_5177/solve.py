import sys
sys.stdin = open('input.txt')
"""

"""
for t in range(int(input())):
    n = int(input())
    heap = [0]
    nums = [*map(int,input().split())]
    for i in range(1,n+1):
        heap.append(nums[i-1])
        while i//2:
            parent = i//2
            if heap[parent] > heap[i]:
                heap[parent], heap[i] = heap[i], heap[parent]
            else: break
            i //= 2
    while n // 2:
        parent = n // 2
        heap[0] += heap[parent]
        n //= 2
    print(f'#{t+1} {heap[0]}')