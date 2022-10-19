"""
활주로
NxN 활주로
각 칸은 높이
가로 or 세로 방향 건설 가능성 확인
높아가 기본적으로 같아야하며, 다르면 경사로 필요 (높이 1 길이 x) 2<= x <= 4
경사로의 길이 x, 높이가 주어질 떄 활주로 건설 가능한 경우의 수는
"""
import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    n,x = map(int,input().split())
    grid = [[*map(int,input().split())] for _ in range(n)]
    tgrid = [*zip(*grid)]
    tgrid = [list(i) for i in tgrid]
    # print(*tgrid,sep='\n')
    cnt = 0
    def dfs(arr,idx = 0): #flag = -1이면 낮아졌었다, +1이면 높아졌었다.
        global cnt
        for i in range(idx+1,n):
            if arr[i] == arr[i-1]:
                continue
            elif arr[i] == arr[i-1] + 1: # 높아지면
                if i >= 2*x and arr[i-2*x:i] == [arr[i-1]]*(2*x): #경사로가 안겹쳐야함. 충분히 멀다면.
                    return dfs(arr,i+1)
                if i >= x and arr[i-x:i] == [arr[i-1]]*x: #앞에 길이가 충분하고, 앞 부분 높이가 같아야함.
                    return dfs(arr,i+1)
                break
            elif arr[i] == arr[i-1] - 1: #낮아지면
                if i+x <= n and arr[i:i+x] == [arr[i]]*x: #뒤로 길이가 충분해야함
                    return dfs(arr,i+x-1)
                break
            else:
                break
        else:
            print(arr)
            cnt += 1
            return 0
    #
    # for i in range(n):
    #     dfs(grid[i])
    #     dfs(tgrid[i])
    dfs([2, 2, 1, 1, 1, 1, 1, 1, 2])

    print(cnt)








