"""
주식
아래의 행동이 가능하다.(매일 3가지중 하나)
날짜와 날짜별 주가가 주어질 때 아래 행동으로 가능한 최대 이익은?
1. 주식 하나를 산다
2. 원하는 만큼 가진 주식을 판다
3. 아무것도 안한다.
2~100만일까지 주어짐.

최대값인 날짜 가격에 앞날의 모든 주식 구매후 판매하면 그게 최대 이득.
1차시도 91퍼 시간초과
2차시도 마찬가지
3차시도 매번 정렬하여 확인하니 시간 초과 ㅋ 8%
4차시도 분명 시간 줄인거 같은데 초과뜨네 ;
5차시도 온갖 시도를 하는데 계속 시간초과 뜨냐 아오
6차시도 ... 내가 생각해도 지리는 최적화 ...
첫 max를 구할 때, max값 후보 index를 받아와서 계산.
"""
o = open('input.txt')
for t in range(int(next(o))):
    n = int(next(o))
    nums = [*map(int,next(o).split())]
    sur=i=0
    maxes = [n-1]
    maxdex = n - 1
    c = 0
    end = 0
    for j in range(n - 2, -1, -1):
        if nums[maxdex] < nums[j]:
            maxdex = j
            c += 1
            maxes.append(maxdex) # 뒤에서 부터 존재하는 max값 후보들 받아오기
    if c == n - 1:
        print(0)
    else:
        while maxes:
            nos = maxes.pop()
            if n - nos == len(maxes): break # 남은 max 후보들이 남은 nums 개수가 같다면.
            maxv = nums[nos]
            sur += maxv*(nos-i) - sum(nums[i:nos])
            i = nos+1
        print(sur)