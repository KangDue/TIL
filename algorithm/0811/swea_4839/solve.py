import sys
sys.stdin = open('input.txt')
#binary search
#edge case 는 차이가 1이 되었을때 답을 찾거나 무한 반복하거나임. 그때 제한걸기
def bifind(a,p):
    l,r = 1,p
    c = int((l+r)/2) # center 값
    count = 0
    while 1:
        if a == c:
            count +=1
            return count
        elif a < c:
            r = c
            c = int((l+r)/2)
            count += 1
            if c-l == 1: #edge 예외처리
                if a == c:
                    count+=1
                return count
        elif a > c:
            l = c
            c = int((l+r)/2)
            count += 1
            if r-c == 1: #edge 예외처리
                if a == c:
                    count += 1
                return count

T = int(input())
for t in range(1,T+1):
    p,a,b=map(int,input().split())#전체 쪽수, a,b가 찾는 쪽
    #a,b 중 누가 더 빠를까? 진짜 search까지 할 필요 x
    ac = bifind(a,p)
    bc = bifind(b,p)
    if ac == bc:
        print(f'#{t} 0')
    elif ac>bc:
        print(f'#{t} B')
    else:
        print(f'#{t} A')