# import sys
# sys.stdin = open('input.txt')
"""
최대 힙
1. push = 배열에 자연수 x를 넣는다.
2. pop = 배열에 가장 큰 값을 출력하고 그 값을 배열에서 제거한다.
첫줄에는 연산의 개수 N, 자연수는 배열 추가, 0은 배열에서 제거.
"""
#입력시간 input으로 하나하나 받아오니 시간초과떠서 한번에 가져왔음.
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
            if heap[idx] > heap[idx//2]: # 부모노드보다 값이 크면 교체
                heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            else: break #안크면 교체 할 필요가 없다.
            idx //= 2
    else: #pop
        if len(heap) > 1:print(heap[1]);heap[1]=0
        else: print(0);continue
        idx = 1
        while 1:
            l = len(heap)
            if 2*idx+1 < l: #오른쪽 노드가 있을 때
                if heap[2*idx+1] > heap[2*idx]:#오른쪽이 더 크면
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