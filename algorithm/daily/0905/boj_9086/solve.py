import sys
sys.stdin = open('input.txt')
for i in range(int(input())):
    temp = input()
    print(temp[0]+temp[-1])
