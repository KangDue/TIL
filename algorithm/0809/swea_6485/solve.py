import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    n = int(input())
    stops = [list(map(int,input().split())) for i in range(n)]
    p = int(input())
    nums = [int(input()) for i in range(p)]
    stations = {i:0 for i in range(1,5001)}
    for i in stops:
        for k in range(i[0],i[1]+1):
            stations[k] += 1
    nums = [stations[i] for i in nums]
    nums = str(nums)[1:-1].replace(",","")
    print(f'#{t} {nums}')

