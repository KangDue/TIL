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
    n = int(sr())
    side = [[*map(int,sr().split())] for _ in range(6)]#동서남북 = 1234
    #변에 수직인 방향이 아니라 변을 따라가는 방향
    # 1,3 가 2개씩 ㄱ 형, 1,4이 2개씩 반전 ㄱ형
    # 2,4 가 2개씩 ㄴ 형, 2,3이 2개씩 반전 ㄴ형
    shape = [[] for i in range(5)]
    for i in side:
        shape[i[0]].append(i[1])
    side = side + [side[0]]#카운팅 했으니 순환용 교체

    if len(shape[1])+len(shape[3]) == 4:#ㄱ #1,3이 연속인게 빈부분
        for i in range(6):
            if side[i][0] == 1 and side[(i+1)][0] == 3:
                a,b = side[i][1],side[(i+1)][1]
                break
        area = shape[4][0]*shape[2][0] - a*b

    elif len(shape[1])+len(shape[4]) == 4:#r
        for i in range(6):
            if side[i][0] == 4 and side[(i+1)][0] == 1:
                a,b = side[i][1],side[(i+1)][1]
                break
        area = shape[3][0]*shape[2][0] - a*b

    elif len(shape[2])+len(shape[4]) == 4:#ㄴ
        for i in range(6):
            if side[i][0] == 2 and side[(i+1)][0] == 4:
                a,b = side[i][1],side[(i+1)][1]
                break
        area = shape[1][0]*shape[3][0] - a*b

    elif len(shape[2])+len(shape[3]) == 4:#Rㄴ
        for i in range(6):
            if side[i][0] == 3 and side[(i+1)][0] == 2:
                a,b = side[i][1],side[(i+1)][1]
                break
        area = shape[1][0]*shape[4][0] - a*b
    print(area*n)