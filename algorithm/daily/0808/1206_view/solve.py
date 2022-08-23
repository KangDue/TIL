import sys
sys.stdin = open('input.txt')
for t in range(1,10+1):
    n = int(input())
    build = list(map(int,input().split()))
    tot = []
    for i in range(2,n-2):#오른쪽 두칸 비워짐
        neighbor = iter( (build[i+1],build[i-1],build[i-2],build[i+2]) ) #iter 써보고 싶어서 써봤습니다.
        diff = 255 # min difference 구하기 위한 초기값
        for k in range(4):
            temp = build[i] - next(neighbor)
            if temp > 0: #낮은 층이 있을때
                if diff > temp: #값 갱신
                    diff = temp
            else: #하나라도 음수면 끝
                break
        else:#무사히 for문 끝난값만 추가
            tot.append(diff)
    print(f'#{t} {sum(tot)}')
