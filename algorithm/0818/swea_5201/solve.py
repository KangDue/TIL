import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1,int(input()) +1 ):
    n, m = map(int,input().split())
    cont = sorted(list(map(int,input().split())), reverse= True) #패딩 오류 방지용
    truck = sorted(list(map(int,input().split())))
    ans = 0
    for i in range(m):
        for k in range(n):
            if truck[i] >= cont[k]:
                ans += cont[k]
                cont[k] = 51 #최대 무게 50이므로 싫지 못하게 51로 변경
                break
    print(f'#{t} {ans}')

