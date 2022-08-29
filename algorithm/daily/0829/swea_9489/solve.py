import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n,m = map(int,input().split())
    pic = [input().replace(' ','') for i in range(n)]
    tpic = [''.join(i).split('0') for i in zip(*pic)]
    pic = [i.split('0') for i in pic]
    tot = sum(pic+tpic,start=[])
    print(f'#{tc+1} {len(max(tot,key=lambda x:len(x)))}')
