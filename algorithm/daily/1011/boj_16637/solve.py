"""
괄호추가하기
주어진 식에서 계산을 무조건 앞에서 부터 순서대로 할 때
괄호를 적절히 씌워서(무조건 연산자 1개)
식의 최대값을 구하시오!
더 빠르게 찾기위해 이것저것 규칙추가 가능하겠지만 그냥 브루트 포스 갈기자
중첩괄호 불가능
"""
import sys
sys.stdin = open('input.txt')

from itertools import combinations as cb
n = int(input())
ex = [*map(lambda x: int(x) if x.isdigit() else x, input())]
ops = {'*':lambda x,y:x*y, '+':lambda x,y:x+y, '-':lambda x,y:x-y}
def cal(arr):
    result = arr[0]
    for i in range(1,len(arr),2):
        result = ops[arr[i]](result,arr[i+1])
    return result

def check(arr,length):
    for i in range(length-1):
        if arr[i] + 2 == arr[i+1]:
            return False
    return True

def make_ex(arr):
    nex=[]
    if arr:
        idx = 0
        for i in arr:
            nex += ex[idx:i-1]+[ops[ex[i]](ex[i-1],ex[i+1])]
            idx = i+2
        nex += ex[i+2:]
        return nex
    else:
        return ex

if n == 1:
    print(ex[0])
else:
    idxes = range(1,n,2)
    visited = [0]*n
    maxv=-2<<31
    for i in range(n//2):
        for comb in cb(idxes,i):
            if not check(comb,i):
                continue
            maxv = max(maxv, cal(make_ex(comb)))
    print(maxv)



j=int
def g(x,y,c):return x+y if c=='+'else x-y if c=='-'else x*y
def f(i,c):return c if i>=n else max(f(i+2,g(c,j(s[i]),s[i-1])),f(i+4,g(c,g(j(s[i]),j(s[i+2]),s[i+1]),s[i-1]))if i<n-2 else -99)
n,s=j(input()),input()
print(f(2,j(s[0])))

