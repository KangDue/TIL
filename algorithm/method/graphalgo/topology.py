inputs=[
    [1,2],
    [1,5],
    [2,3],
    [3,4],
    [4,6],
    [5,6],
    [6,7],
    #[4,2] #순환그래프 만드는 edge 추가해서 결과 보기
] # edge 정보 (DAG)
"""
 topological sort는
1. 주어진 그래프가 acyclic한지?
2. acyclic 할 때 위상 정렬 결과를 반환.

acyclic하지 않다면 출발점 이라는 개념이 없어서 
위상정렬이 불가능하다.
그리고 진입차수가 0인게 안생김. 서로 물려있어서 0이 안되기 때문.
그래서 N개 노드를 방문하기 전에 q가 비어버리면 cycle이 있는것.

시간 복잡도는 O(V + E) (정점의수 + 간선의 수) 인 매우 빠른 알고리즘.
"""
from collections import deque,defaultdict

n = 7
degree = defaultdict(int) #진입 차수
graph = [[] for _ in range(n+1)] # 그래프
result = [] #정렬 결과
for x,y in inputs: #그래프 생성 및 진입차수 업데이트
    graph[x].append(y)
    if not degree.get(x):
        degree[x] = 0
    degree[y] += 1
for i in degree: # 진입차수 0인 시작접 하나 뽑기
    if not degree[i]:
        start = i
        break
q = deque([start])
degree.pop(start)
while q:
    now = q.popleft()
    result.append(now) # result에 정렬 순서대로 추가
    temp = []
    for nv in graph[now]: # 연결된 간선 제거
        degree[nv] -= 1
    for i in degree: # degree 다시 확인하며 진입차수 0인건 q에 추가
        if not degree[i]:
            q.append(i)
            temp.append(i)
    for i in temp: #degree에서 q에 넣은 녀석들은 삭제.
        degree.pop(i)
if degree: #degree가 안 비었다는건 cyclic하다는 뜻
    print("순환 그래프입니다.")
else:
    print("위상정렬 결과입니다.")
    print(result)
