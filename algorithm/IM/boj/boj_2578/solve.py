import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
숫자 몇개를 불러야 3빙고를 할까?
"""
if __name__ == "__main__":
    import sys
    def check(x):#불러서 그린 숫자 기준 카운트
        for i in range(25): #위치 찾기, 무조건 존재는 한다.
            if line_bg[i] == x:
                break
        row,col = divmod(i,5)
        bg[row][col]=0
        if row == 4-col: #우상 좌하 대각선, 5개뿐인데 why not? 다쓰자
            t1=t2=t3=0
            for i in range(5):
                t1+=bg[4-i][i]
                t2+=bg[row][i]
                t3+=bg[i][col]
            return [t1,t2,t3].count(0)
        elif row==col: #좌상 우하 대각선
            t1=t2=t3=0
            for i in range(5):
                t1+=bg[i][i]
                t2+=bg[row][i]
                t3+=bg[i][col]
            return [t1,t2,t3].count(0)
        else: #나머지 위치
            t2=t3=0
            for i in range(5):
                t2+=bg[row][i]
                t3+=bg[i][col]
            return [t2,t3].count(0)
    sr = sys.stdin.readline
    bg = [[*map(int,sr().split())] for i in range(5)] # 빙고판
    line_bg = sum(bg,start=[]) # 숫자 찾기용
    ch = [*map(int,sum([sr().split() for i in range(5)],start=[]))] # 사회자
    #line_bg 에서 divmod(idx,5) = row,col이다.
    c = 0
    for i in range(25):
        c += check(ch[i])
        if c >= 3:
            break
    print(i+1)
