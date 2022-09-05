import sys
sys.stdin = open('input.txt')
def At(a, b):
    return (a+b)*(a-b)
a,b = map(int,input().split())
print(At(a,b))