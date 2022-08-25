import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
최소 면적의 창고 만들기. 움푹파인 곳이 없고 딱맞게 창고를 둘러싼 다각형
"""
if __name__ == "__main__":
    import sys
    r=range
    sr = sys.stdin.readline
    def totminus(x0,x1,h):#a~b까지 뺄셈하고 끝이 0이면 버린다.
        for i in range(x0,x1+1):
            obs[i][1] -= h
        return (obs[x1][0] - obs[x0][0] + 1) * h
    n = int(sr())
    obs = sorted([[*map(int,sr().split())] for i in r(n)])#왼쪽면의 위치, 높이
    obs = [[0,0]] + obs
    ans = 0
    x0, x1 = 0, len(obs) - 1  # 시작,
    while x1:
        pivot = min(obs[x0][1], obs[x1][1])
        ans += totminus(x0,x1,pivot)
        while obs[x0][1] <= 0 and x0 < n: x0 += 1
        while obs[x1][1] <= 0 and x1 > 0: x1 -= 1
    #print(obs, x0, x1, ans)
    print(ans)