# 보석 도둑 - 배낭 문제랑 비슷한 듯
# 담을 수 있는 보석의 최대 가격은?
# 최대 30만개 까지 주어짐.
# 가방이 자기가 담을 수 있는 것중 가장 비싼 것을 담아야 함.
# 가방에 담는 순서는
import heapq
o = open('input.txt')
N, K = map(int,next(o).split())
jew = [] # 보석 무게, 가치
for _ in range(N):
    weight,val = map(int,next(o).split())
    heapq.heappush(jew,(weight,val))
bag = sorted([int(next(o)) for _ in range(K)]) # 가방의 최대 무게, 오름 차순
# print(jew) #가치순, 무게순 (역순) 정렬 비싼 순서중 무거운거 부터.
# print(bag)
ans = 0
temp = []
# print(jew)
for j in range(K):
    while jew and bag[j] >= jew[0][0]:
        heapq.heappush(temp, -heapq.heappop(jew)[1]) #max heap 구성
    #가벼운 것들 중 가치가 제일 높은 것
    if temp: #가방 max 보다 가벼운 것들 목록
        ans -= heapq.heappop(temp)
    elif not jew: #가방에 담을 수 있는게 없다면
        break
print(ans)