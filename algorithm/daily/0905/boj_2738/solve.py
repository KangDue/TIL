import sys
sys.stdin = open('input.txt')

import sys
read = sys.stdin.readline
n, m = map(int,read().split())#행, 열
temp1 = [[] for _ in range(n)]
temp2 = [[] for _ in range(n)]
temp =[temp1,temp2]
for i in range(2):
    for j in range(n):
        temp[i][j] = [*map(int,read().split())]
for i in zip(temp1,temp2):
    print(*map(lambda x: sum(x),zip(*i)))
# print(*map(lambda x:sum(x),))
