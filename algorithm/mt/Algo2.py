import sys
sys.stdin = open('algo2_sample_in.txt')
def match(x):
    global grid,n
    c = 0 #패턴일치 개수 c
    for i in range(n-2): #패턴 크기 고려 범위 설정
        for j in range(n-2):
            for a in range(3):#패턴 확인을 위한 2중 for문
                mode = 0 #break를 위한 mode
                for b in range(3):
                    if grid[i+a][j+b] != x[a][b]:#패턴 불일치시 break
                        mode = 1 # 패턴 불일치시 반복문 2개 탈출
                        break
                if mode:# 패턴 불일치시 반복문 2개 탈출
                    break
            else:#패턴이 일치하면  c+=1 (2중 for문 무사 완료시)
                c += 1
    return c

for t in range(1,int(input())+1):
    n = int(input())
    grid = [list(map(int,input().split())) for i in range(n)]
    pattern = [list(map(int,input().split())) for i in range(3)]
    print(f'#{t} {match(pattern)}')