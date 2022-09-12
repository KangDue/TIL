"""
요세푸스의 문제
1~N번까지 N명으로 만든 원에서 K 번째 사람을 뺀다.
이때 빠지는 사람의 순서를 요세푸스 순열이라 한다.
사람 빠질때마다 순서가 좁혀진다.
"""
import sys
sys.stdin = open('input.txt')
#양방향 큐 만들면 삽가능이지만 크기가 작아서 리스트도 충분
n,k = map(int,input().split())
people = list(range(1,n+1))
pick = 0
ans = []
while n:
    pick = (pick + k - 1) % n
    ans.append(people.pop(pick))
    n-=1
print('<'+str(ans)[1:-1]+'>')