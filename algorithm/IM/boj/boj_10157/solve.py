import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
ㄱ 0,90,180,270 돌린 모양의 육각형 참외밭 넓이 구하기
어떤 꼭짓점을 기준으로 반시계방향으로 돌며
변을 따라가는 방향(동서남북=1234)와 각 변의 길이가 주어질때
면적에 단위넓이당 참외 수를 곱한 결과 출력 
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n,k = map(int,sr().split())# nxk mat
    target = int(sr())
    def snail():
        global pos,a,b,k
        vec = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cv = 0
        while pos < n*k:
            while mat[a+vec[cv%4][0]][b + vec[cv%4][1]] == 0:
                pos += 1
                a += vec[cv%4][0]
                b += vec[cv%4][1]
                mat[a][b] = pos
                if pos == target: return a,b
            cv += 1
        else: return [0]

    mat = [[-1]+[0 for _ in range(k)]+[-1] for _ in range(n)]
    mat = [[-1]*(k+2)] + mat + [[-1]*(k+2)]
    pos = 1
    a,b=1,1
    mat[a][b] = pos
    if pos == target:
        print(a,b)
    else:
        print(*snail())



