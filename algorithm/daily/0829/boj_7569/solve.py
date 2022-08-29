import sys
sys.stdin = open('input.txt')
"""
토마토 2 (3D버전)
토마토를 보관하는 큰 창고를 가지고 있다.
MxNxH상자에 담겨있다.
하루가 지나면 익은 토마토 옆 설익은 것들이 익는다.(전파)(상하좌우위아래)
며칠이 지나면 모두 익는지 최소 일수를 구하시오.
모든 토마토가 익으면 0, 익지 못하면 -1, 첨부터 전부 익어있다면? 1
토마토 = 1, 안 익은 토마토 = 0, 없으면 -1
"""
from collections import deque
C,R,H = map(int,input().split())
tomato = [[[*map(int,input().split())] for _ in range(R)] for _ in range(H)]
print(tomato[0])
