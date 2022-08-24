import sys
sys.stdin = open('input.txt')
def disc(s): #숫자 갯수를 카운팅, 중복시 바로 종료
    for i in r(9):
        tb1=[0]*10
        tb2=[0]*10
        for j in r(9):#가로세로 확인
            if tb1[s[i][j]]:return 0
            if tb2[s[j][i]]:return 0
            tb1[s[i][j]]=1
            tb2[s[j][i]]=1
            if i%3+j%3==0: # 작은 3x3 시작점이면
                tb3=[0]*10
                for a in r(3):
                    for b in r(3):
                        if tb3[s[i+a][j+b]]:return 0
                        tb3[s[i+a][j+b]]=1
    return 1

d,w,r=int,input,range
for t in r(d(w())): #어떻게 스도쿠를 확인할까???
    s=[]
    for i in r(9):
        s.append(list(map(d,w().split())))
    print(f'#{t+1} {disc(s)}')#이상 없으면