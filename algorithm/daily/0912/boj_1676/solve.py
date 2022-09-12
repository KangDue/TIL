import sys
sys.stdin = open('input.txt')
#n!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때 까지 0의 개수
from math import factorial as f
from itertools import takewhile as t
n=int(input())
a=str(f(n))[::-1]
print(len(list(t(lambda x:x=='0',a))))

#숏버전
# print(len(list(t(lambda x:x=='0',str(f(int(input())))[::-1]))))

#while버전
# n,c=f(int(input())),0
# while n:
#     n,b=divmod(n,10)
#     if b:print(c);break
#     else:c+=1

#백준랭킹권 숏코딩
# n=int(input())//5
# print(n+n//5+n//25)