"""
총 N개의 꽃 이 있는데, 모두 같은 해에 피어서 같은 해에 진다.
하나의 꽃은 피는 날과 지는 날이 정해져 있다.
ex)0508 ~ 0613인 꽃은 0612까지는 꽃이 핀 상태이다.
4,6,9,11월은 30일 까지 있고
1,3,5,7,8,10,12 는 31일 까지
2월은 28일까지
이 꽃들 중 아래 조건을 만족하는 꽃들을 선택하고 싶다.
1. 3.1 ~ 11.30까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
2. 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다.
선택한 꽃들의 개수를 최소일때 꽃의 개수는 ?
선택 불가 하면 0 출력

꽂들은 1 ~ 10만개가 주어진다.
<접근>
1. 피는 날짜가 빠르고, 지는 날짜가 늦은 순으로 정렬
#수정해도 44%에서 틀리누 ; 왜이러니

#빠르게 푼사람 풀이를 보면
이양반은 dict로 달별로 묶어놓고 max를 추출함.
나처럼 반복문으로 안뽑음.
그리고 날짜를 적절하게 달*100 + 일 이렇게 변환해 사용.
"""
# calendar = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# print(*flowers,sep= '\n')
o = open('input.txt')
flowers = []
n = int(next(o))
for _ in range(n):
    a,b,c,d = map(int,next(o).split())
    flowers.append((a,b,c,d))
flowers.sort()
pa,pb = 3, 1
i = 0
idx = 0
count = 0
maxv = (0, 0, 0, 0)
while 1:
    for i in range(idx,n):
        if flowers[i][0] > pa or (flowers[i][0] == pa and flowers[i][1] > pb):
            break
        maxv = max(maxv,flowers[i],key = lambda x:(x[2],x[3]))
    if count > idx: break
    count += 1
    idx = i
    pa,pb = maxv[-2],maxv[-1]
    if pa == 12:
        break

if maxv[2] == 12:
    print(count)
else:
    print(0)

