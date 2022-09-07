import sys
sys.stdin = open('input.txt')
#666이 들어간 숫자 순서대로

n = int(input())
c = 0
i = 666
while 1:
    if str(i).find('666') > -1:
        c += 1
    if c == n:
        print(i)
        break
    i += 1