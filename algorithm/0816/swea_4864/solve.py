import sys
sys.stdin = open('input.txt',encoding='utf-8')

#문자열 a,b가 주어질때 a가 b에 있는지 판별
ip = input
for t in range(1,int(ip())+1):
    a,b = ip(),ip()
    if b.find(a) > -1: print(f'#{t} 1')
    else: print(f'#{t} 0')