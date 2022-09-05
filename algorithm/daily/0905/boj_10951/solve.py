import sys
sys.stdin = open('input.txt')
while 1:
    try:
        a, b = map(int,input().split())
        if a and b:
            print(a+b)
    except:break
