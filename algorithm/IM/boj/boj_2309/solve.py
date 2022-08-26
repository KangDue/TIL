import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
9명의 난쟁이중 키의 합이 100인 경우 출력
"""
from itertools import combinations as cb
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    so = sorted([int(sr()) for i in range(9)])
    for i in cb(so,7):
        if sum(i)==100:break
    print(*i,sep='\n')



