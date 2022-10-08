"""
개리맨더링
그래프가 있을 때,
두개의 그룹이 있고
한 그룹은 적어도 하나의 노드를 포함한다.
그룹은 서로 이어져있어야한다.
두 그룹의 인구차이를 최소로 할때 값을 구하자!.
- 위상정렬하고 자르면 될듯?
"""
import sys
sys.stdin = open('input.txt')

from itertools import combinations as cb
n = int(input())
population = [0]+[*map(int,input().split())] #1번부터
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    a,*b = map(int,input().split())
    graph[i].extend(b)

#경우의 수로 가즈아~
group = 0
visited = [0]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        group += 1
        q = [i]
        visited[i]=i
        while q:
            new = []
            for k in q:
                for nv in graph[k]:
                    if not visited[nv]:
                        visited[nv] = i
                        new.append(nv)
            q = new
# print(visited)

if group == 2:
    ans = 0
    for i in range(1,n+1):
        if visited[i]==1:
            ans += population[i]
        else:
            ans -= population[i]
    print(abs(ans))

elif group > 2:
    print(-1)

else: #spanning tree
    minv = int(1e9)
    for i in range(1,n): #1개부터 n-1개 까지 뽑기, 나머지는 다른 그룹
        for g1 in cb(range(1,n+1),i): #i개 뽑기
            visited = [2]*(n+1)
            g2 = []
            for j in range(1,n+1):
                if j in g1:
                    visited[j] = 0
                else:
                    g2.append(j)
            q = [g1[0]]
            visited[g1[0]] = 1
            temp = 1
            A = population[g1[0]]
            while q:
                new = []
                for k in q:
                    for nv in graph[k]:
                        if not visited[nv]:
                            visited[nv] = 1
                            new.append(nv)
                            temp += 1
                            A += population[nv]
                q = new
            if temp == i: #한 그룹일 때
                q = [g2[0]]
                visited[g2[0]] = 1
                temp2 = 1
                B = population[g2[0]]
                while q:
                    new = []
                    for k in q:
                        for nv in graph[k]:
                            if visited[nv] !=1:
                                visited[nv] = 1
                                new.append(nv)
                                temp2 += 1
                                B += population[nv]
                    q = new
                if temp+temp2 == n:
                    minv = min(minv,abs(A-B))
    print(minv)