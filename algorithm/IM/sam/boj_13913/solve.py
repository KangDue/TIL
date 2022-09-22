import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
숨바꼭질3 에서는 순간이동시 시간이 0초 필요해서 최단거리 역전이 되지만
4는 x
"""
if __name__ == "__main__":
    import sys
    r, sr = range, sys.stdin.readline
    from collections import deque,defaultdict
    n,k = map(int,sr().split())
    nums = [0]*100001
    visited = [0]*100001
    q = deque([[0,n]])
    dist=defaultdict(int)
    while q:
        time,v = q.popleft()
        #최단거리니까 중복 가줄 필요 없다.
        if v==k:#최단거리 출력#break 때려버리면 최단거리가 아님.
            break
        for i in (2*v,v+1,v-1):#한 칸 갈때
            if 0<= i <= 100000 and visited[i] == 0:
                q.append([time+1,i])
                visited[i] = 1
                dist[i]=v #바로 앞 경로를 기억한다.
    temp = k
    path = []
    while temp != n:
        path.append(temp)
        temp = dist[temp]
    path.append(n)
    path.reverse()
    print(len(path)-1)
    print(*path)

#
# #이 문제에 특화된 풀이
# def F(N,K):
#     if N>=K: # N이 K보다 커지면 거리 차이만큼이 필요한 시간/ 거치는 곳도 그 range의 reverse로 표현 됨.
#         return N-K,[*range(N,K-1,-1)]
#     elif K==1: # n 이 0이고 k == 1이면 1초면 가고 0,1임
#         return 1,[0,1]
#     elif K%p2:#n이 k보다 작고 K가 짝수면
#         A=F(N,K-1) #한스텝 빽
#         B=F(N,K+1) #한스텝 앞으로
#         if A[0]<B[0]: #둘 중 더 시간이 짧게 드는쪽으로
#             return A[0]+1, A[1]+[K] #현재 k로 가는 시간과 경로를 추가
#         else:# 그 반대
#             return B[0]+1, B[1]+[K]
#     else: #n이 k보다 작고 k가 홀수면
#         B=F(N,K//p2)
#         if K-N<B[0]+1: #지금까지 걸린 시간 + 1 보다 K-N이 더 크면 도달 시간과 n~k 수열 반환
#             return K-N,[*range(N,K+1)]
#         else:# k-n이 더 작아졌다면 k만 더하면 끝
#             return B[0]+1,B[1]+[K]
# N,K=map(int,input().split())
# R=F(N,1)
# print(R[0])
# print(*R[1])