import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 안타깝게도 파이썬 답 제출은 없는 문제...
def twopick(x, n):
    for i in range(len(x)):
        if n == 1:
            yield [x[i]]
        else:
            for next in twopick(x[i + 1:], n - 1):
                yield [x[i]] + next
import math
answers = []
for t in range(1, int(input())+1):
    N = int(input())
    cities = [tuple(map(int,input().split())) for i in range(N)]
    info = [[i,[]] for i in range(N)] # 0~ N-1번 도시로 구분
    result = {i:0 for i in range(N)}
    for i in twopick(range(N),2): #각 도시별 두가지 씩 뽑기, 두 도시간 위협은 단방향이다.
        dist = math.pow(cities[i[0]][0]-cities[i[1]][0],2) + math.pow(cities[i[0]][1]-cities[i[1]][1],2)
        power1 = cities[i[0]][2]/dist #1의 2를 향한 힘
        power2 = cities[i[1]][2]/dist #2의 1을 향한 힘
        if power1 > cities[i[1]][2]: #1의 power 가 2의 power 보다 크면
            if info[i[1]][1]: # 뭔가 있다면.
                for k in info[i[1]][1][:]: # 같은 도시는 없다.
                    if k[1] < power1:
                        info[i[1]][1].remove(i)
                        continue
                    elif k[1] > power1:#크면 볼 것도 없다.
                        break
                    else: # 파워가 같으면 추가
                        info[i[1]][1].append([i[0], power1])  # 새 도시의 영향력 정보를 추가
            else:  # 안 비어 있다면 일단 추가
                info[i[1]][1].append([i[0], power1])


        if power2 > cities[i[0]][2]: #2의 power 가 1의 power 보다 크면
            if info[i[0]][1]: # 뭔가 있다면.
                for k in info[i[0]][1][:]: # 같은 도시는 없다.
                    if k[1] < power2:
                        info[i[0]][1].remove(i)
                        continue
                    elif k[1] > power2:#크면 볼 것도 없다.
                        break
                    else: # 파워가 같으면 추가
                        info[i[0]][1].append([i[1], power2])  # 새 도시의 영향력 정보를 추가
            else:  # 안 비어 있다면 일단 추가
                info[i[0]][1].append([i[1], power2])
    info.sort(key=lambda x:len(x[1]))
    print(info) #
    for i in range(N): #다른 도시를 따르면 그 도시 번호
        if len(info[i][1]) == 0:
            result[info[i][0]] = "K" #혼자면 군주제
        elif len(info[i][1]) >= 2:
            result[info[i][0]] = "D" # 여러개면 공화제
        elif len(info[i][1]) == 1: #다른거 따르면 그 번호
            result[info[i][0]] = info[i][1][0][0]
    for i in range(N): #뿌리 찾기
        if isinstance(result[i],int):
            temp = (result[i],i)
            while isinstance(temp[0],int):
                temp = (result[temp[0]],temp[0])
            result[i] = temp[1]+1 #번호는 1씩 보정 0~n-1로 해놔서 문제 요건인 1~N으로 보정해줘야함

    print(f'#{t}',*result.values())

#     answers.append(f'#{t} {ans}')
# print(*answers,sep="\n")