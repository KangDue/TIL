import sys
sys.stdin = open('input.txt')
#덩치를 몸무게 x, 키 y일때 (x,y)로 표현
#x,y 둘다 A가 B보다 크면 A가 B보다 덩치가 크다라고 표현
#자기보다 덩치 큰 사람 수 + 1 은 자기 등수
n = int(input())
people = []
for i in range(n):
    people.append([*map(int,input().split())])
people = [ [i]+people[i] for i in range(n)]
ranking = sorted(people,key=lambda x:(x[1],x[2]))
ans = [0]*n
for i in range(n-1):
    rank = 1
    for j in range(i+1,n):
        if ranking[i][1] < ranking[j][1] and ranking[i][2] < ranking[j][2]:
            rank += 1
    ans[ranking[i][0]]=rank
ans[ranking[-1][0]] = 1
print(*ans)