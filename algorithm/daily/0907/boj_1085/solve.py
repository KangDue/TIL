import sys
sys.stdin = open('input.txt')
#직사각형 내부의 현 위치에서 직사각형의 경계선까지 거리의 최소값.
x,y,w,h=map(int,input().split())
print(min(abs(w-x),abs(h-y),x,y))
