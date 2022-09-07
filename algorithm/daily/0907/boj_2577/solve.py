import sys
sys.stdin = open('input.txt')
num = 1
info = [0]*10
for i in range(3):
    num *= int(input())
while num:
    num, rem = divmod(num,10)
    info[rem] += 1
print(*info,sep='\n')