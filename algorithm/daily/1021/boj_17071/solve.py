import sys
sys.stdin = open('input.txt')

import sys
r, sr = range, sys.stdin.readline
n,k = map(int,sr().split())
me = [-1]*500001
me_odd = [-1]*500001
sib = [-1]*500001
if n==k:
    print(0)
else:
    time,step = 0,1
    while k <= 500000: #동생 234837
        sib[k] = time
        k += step
        step += 1
        time += 1

    ans = []

    q = [n]
    me[n] = 0
    a, b = divmod(sib[n], 2)
    if a >= 0 and not b:
        ans.append(sib[n])
    time = 0

    while q:
        new = []
        time += 1
        try:
            for x in q:
                for nx in (x+1,x-1,x*2):
                    if 0<=nx<=500000: # 한 번 간 곳은 다시 갈 수 있다.
                        if not time%2 and me[nx] == -1: # 짝 일때
                            new.append(nx)
                            me[nx] = time
                            a, b = divmod(sib[nx] - me[nx], 2)
                            if a >= 0 and not b:
                                ans.append(sib[nx])
                        elif time%2 and me_odd[nx] == -1: #홀 일때
                            new.append(nx)
                            me_odd[nx] = time
                            a, b = divmod(sib[nx] - me_odd[nx], 2)
                            if a >= 0 and not b:
                                ans.append(sib[nx])
            q=new
        except:
            break
    if ans:
        print(min(ans))
    else:
        print(-1)

#뒤로 이동하진 않는다 ... 문제 참 빡치네
    # me = [[] for i in range(7)]
    # sib = [[] for i in range(7)]
    # sib[0].append(k)
    # me[0].append(n)
    # step = 1
    # for i in range(1,7):
    #     for j in sib[i-1]:
    #         sib[i].append(j + step)
    #     step += 1
    #
    # for i in range(7):
    #     sib[i].sort()
    # print("--------------")
    # for i in range(1,7):
    #     for j in me[i-1]:
    #         me[i].append(2*j)
    #         me[i].append(j - 1)
    #         me[i].append(j + 1)
    # for i in range(7):
    #     me[i].sort()
    #     print(set(me[i])&set(sib[i]))