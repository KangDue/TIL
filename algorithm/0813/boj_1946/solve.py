import sys
sys.stdin = open('input.txt',encoding='utf-8')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    memb = [tuple(map(int,input().split()))  for i in range(N)]
    memb.sort()
    temp = memb[0]
    for i in range(1,N):#무조건 첫과목 자기 앞순위보다 다른 과목 순위가 앞서야 살아남음.
        if memb[i][1]<temp[-1][1]:
            temp.append(memb[i])
    print(len(temp))