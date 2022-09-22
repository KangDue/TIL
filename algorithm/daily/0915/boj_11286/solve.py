# import sys
# sys.stdin = open('input.txt')
"""
절대값 min 힙
1. push = 배열에 정수 x(x!=0)를 넣는다.
p2. pop = 배열에 가장 절대값이 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
첫줄에는 연산의 개수 N, 자연수는 배열 추가, 0은 배열에서 제거.
"""
#입력시간 input으로 하나하나 받아오니 시간초과떠서 한번에 가져왔음.
from math import inf
o = open('input.txt')
n = int(next(o))
heap = [0]
stack = []
for temp in map(int,o):
    if temp: #append
        if stack:
            idx = stack.pop()
            heap[idx] = temp
        else:
            heap.append(temp)
            idx = len(heap)-1
        while idx//2:
            if abs(heap[idx]) < abs(heap[idx//2]): # 부모노드보다 값이 크면 교체
                heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            elif heap[idx]<0 and heap[idx] == -heap[idx//2]:
                heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            else: break #안크면 교체 할 필요가 없다.
            idx //= 2
    else: #pop
       # print(heap)
        if len(heap) > 1 and heap[1]==inf: print(0);continue #조건 중요,
        elif len(heap) > 1: #나는 진짜 삭제가 아니라 값만 교체하는거라 잘 봐야함.
            print(heap[1]);heap[1] = inf
        else: print(0);continue
        idx = 1
        while 1:
            l = len(heap)
            if 2*idx+1 < l: #오른쪽 노드가 있을 때
                if abs(heap[2*idx+1]) < abs(heap[2*idx]) or (heap[2*idx+1] < 0 and heap[2*idx+1] == -heap[2*idx]):#오른쪽이 더 작으면
                    heap[idx], heap[2*idx+1] = heap[2*idx+1], heap[idx]
                    idx = 2*idx + 1
                else:
                    heap[idx], heap[2 * idx] = heap[2 * idx], heap[idx]
                    idx = 2 * idx
            elif 2*idx < l:#왼쪽 노드만 있을 때
                heap[idx], heap[2 * idx] = heap[2 * idx], heap[idx]
                idx = 2 * idx
            else:
                stack.append(idx)
                break #말단(leaf)