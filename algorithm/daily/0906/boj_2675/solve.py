import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    n, text = input().split()
    temp=''
    n = int(n)
    for i in text:
        temp+=i*n
    print(temp)