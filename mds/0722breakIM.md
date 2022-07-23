# List 1

```python
#N개의 양의정수 중에서 가장 큰수와 가장 작은수의 차이.
#1<= N <=1000000
T = int(input())
for t in range(1,T+1):
  n = int(input())
  nums = list(map(int,input().split()))
  maxv = 0
  for i in nums:
    if maxv < i:
      maxv = i
  minv = 1000000
  for i in nums:
    if minv > i:
      minv = i
  print(f'#{t} {maxv-minv}')

# 전기버스 종점까지 최소 충전수
T = int(input())
for t in range(1,T+1):
    k,n,m = map(int,input().split())
    # 한번충전 이동가능 정류장 수, 0~n번 정류장, 충전 정류장
    supply = list(map(int,input().split()))
    temp = [False]*(n+1)
    for i in range(n+1):
      if i in supply:
        temp[i] = True

    count = 0
    where = k
    while 1:
        if len(temp)-1 <=k:
            break
        else:
            try:
                if any(temp[:k+1]):#한 번 가는 거리안에 충전소 유무
                    temp2 = list(reversed(temp[1:k+1]))
                    temp = temp[k - temp2.index(True)::] #0
                    count += 1
                    where += k - temp2.index(True)
            except:
                break
    if where >= n:
        print(f'#{t} {count}')
    else:
        print(f'#{t} {0}')


 #가장 많이 적힌 수와 그 장수
T = int(input())
for t in range(1,T+1):
    n = int(input()) #카드 장수
    cards = list(map(int,input()))
    count = [0 for i in range(10)]
    for i in cards:
        count[i] += 1
    ans = [(count[i],i) for i in cards]
    print(f'#{t} {max(ans)[1]} {max(ans)[0]}' )         


# 정수 n개 리스트중 연속된 m개의 합을 계산할때
# 가장 큰 경우와 작은 경우의 차이를 출력

T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    maxv = -1
    ans = -1

    for i in range(n-m+1):
        if maxv < sum(nums[i:i+m]):
            maxv = sum(nums[i:i+m])
    for i in range(n-m+1):
        if ans < (maxv - sum(nums[i:i+m]) ):
            ans = (maxv - sum(nums[i:i+m]))
    print(f'#{t} {ans}')

#10x10 grid 상 r,b color 좌상,우하 좌표로 사각형
#좌표가 그냥 cartesian 이 아니라 marix index 처럼하니 주의... 2,2, 4,4 넓이 = 9
#을 나타낼때 둘이 겹쳐 purple이 되는 영역 넓이 구하기
#그리드 1x1은 넓이 1
def fill(cord,grid):
    for i in range(cord[0],cord[2]+1):
        for k in range(cord[1],cord[3]+1):
            #좌표랑 행열 인덱스 반대임
            if grid[k][i] == cord[4]: #같은색이면 패스
                pass
            else:
                grid[k][i] += cord[4] # 다른색이면 덧칠
    return grid

T = int(input())
for t in range(1,T+1):
    n = int(input()) # 사각형 수
    grid = [[0 for i in range(11)] for k in range(11)] # 계산 편하게 11x11로 생성
    recs = [ list(map(int,input().split())) for i in range(n)]
    for i in recs:
        grid = fill(i,grid)
    ans = 0
    for i in grid:
        ans += i.count(3)
    print(f'#{t} {ans}')

#1~12 자연수로 이루어진 집합A
#이중 원소가 N개 원소의 합이 K인 부분집합 갯수
#없으면 0 - brute force로 품.
def bin_gen(k):
    bin_list = []
    for i in range(2**12):
       bin_list.append(list(map(int,f'{int(bin(i)[2:]):0{12}d}')) )
    bin_list = list(filter(lambda x: sum(x)==k,bin_list))
    return bin_list
def list_mul(a,b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans         

T = int(input())
for t in range(1,T+1):
    a = list(range(1,13))
    n,k = map(int,input().split())
    b_l = bin_gen(n)
    count = 0
    for i in b_l:
        temp = list_mul(a,i)
        if temp == k:
            count += 1
    print(f'#{t} {count}')    

#binary search
def bifind(a,p):
    l,r = 1,p
    c = int((l+r)/2) # center 값
    count = 0
    while 1:
        if a == c:
            count +=1
            return count
        elif a < c:
            r = c
            c = int((l+r)/2)
            count += 1
        elif a > c:
            l = c
            c = int((l+r)/2)
            count += 1
T = int(input())
for t in range(1,T+1):
    p,a,b=map(int,input().split())#전체 쪽수, a,b가 찾는 쪽
    #a,b 중 누가 더 빠를까? 진짜 search까지 할 필요 x
    ac = bifind(a,p)
    bc = bifind(b,p)
    if ac == bc:
        print(f'#{t} 0')
    elif ac>bc:
        print(f'#{t} B')
    else:
        print(f'#{t} A')

#색다른 정렬
#max1,min1,max2,min2 ... 정렬
#정렬 결과는 10개까지만 출력
T = int(input())
for t in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    mode = True
    for i in range(10): # 10개 까지만 정렬
        for k in range(-1,-n+i,-1):
            if mode:#max가져다 놓기
                if nums[k] > nums[k-1]:
                    nums[k] ,nums[k-1] = nums[k-1],nums[k]
            else:#min 가져다 놓기
                if nums[k] < nums[k-1]:
                    nums[k] ,nums[k-1] = nums[k-1],nums[k]
        mode = False if mode else True
    print(f'#{t} {str(nums[:10])[1:-1].replace(",","")}')



```
