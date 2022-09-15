import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    e,n = map(int,input().split())
    graph=[[] for _ in range(e+2)]
    a=[*map(lambda x:int(x),input().split())]
    for i in range(0,2*e,2):
            graph[a[i]].append(a[i+1])
    ans = 1
    stack = [n]
    while stack:
        for i in graph[stack.pop()]:
            stack.append(i)
            ans += 1
    print(f'#{t+1} {ans}')