import sys
sys.stdin = open('input.txt')
from collections import deque
for t in range(int(input())):
    n, idx = map(int, input().split())
    docs = [*map(int,input().split())]
    docs = [(docs[i],i) for i in range(n)] #우선순위,문서번호
    q = deque(docs)
    count = 1
    while q:
        if q[0][0] == max(q)[0]:
            if q[0][1] == idx:
                break
            else:
                q.popleft()
                count += 1
        else:
            q.append(q.popleft())
    print(count)
