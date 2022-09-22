import sys
sys.stdin = open('input.txt')
"""
한 강의 수강생들이 텀프로젝트를 수행한다.
팀원수에는 제한이 없다.
같이 하고 싶은 사람은 한명만 고를 수 있다. 자신도 가능
그래프 구조상 순환이 일어날때만 한팀이 된다. # 방향성 그래프에서 순환판별
팀을 이루지 못한 인원을 출력하라.
#굳이 bfs 아니어도 가능한거 같은데??

입력: 테케수, 학생수, 선택받은 학생들 (1,p2,3~)순서대로 선택
1. 그냥 오류로 처리하니 시간 초과 발생.
p2. 삭제시키는게 나은거 같다.
"""
from collections import deque
for t in range(int(input())):
    n = int(input())
    select = [0]+[*map(int,input().split())]
    graph = {i:select[i] for i in range(1,n+1)}
    #1번부터 확인
    #visited 로 체크하는데 시작점은 체크 안하고 시작, 그래야 순환
    visited = [0]*(n+1)
    temp = 1
    for i in range(1,n+1):
        if visited[i] == 0:#간적 없는 노드만
            while visited[i] == 0:#간적있는거 만날때까지
                visited[i] = temp #몇번 그룹인지 표시
                i = graph[i] #다음 노드로 #
            while visited[i] == temp: #그룹표시 된것중에서, #순환구조라면 다시 자기까지 전부 0이된다.
                visited[i] = -1
                i = graph[i]
            temp += 1
    count = 0
    for v in visited:
        if v>0:
            count+=1
    print(count)

