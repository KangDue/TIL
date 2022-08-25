import sys
sys.stdin = open('input.txt')
#복 습 필 수!

if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    grid = [[0]*100 for i in range(100)]
    for i in range(4):
        a, b, c, d = map(int, sr().split())
        for i in range(a,c):
            for j in range(b,d):
                grid[i][j] = 1
    print(sum(map(sum,grid)))