import sys
sys.stdin = open('input.txt', encoding='utf-8')


for t in range(1,int(input())+1):
    rooms = [0]*200 # 1~400( = 0~399)를 (홀수 ,짝수를 0~199에 쑤셔 넣기) 1 -> 0, 3 -> 1, p2 -> 0, 4 -> 1 변환
    for i in range(int(input())):
        x, y = map(lambda a:(int(a)-1)//2,input().split()) #둘다 1씩 빼서 2로나눈 몫 취해주면 된다.
        x, y = (y, x) if x > y else (x,y) # 오름차순 정렬
        for j in range(x,y+1): #각 path마다 1씩 더해준다. 가장 많이 겹치는 횟수가 답
            rooms[j] += 1
    print(f'#{t} {max(rooms)}')


# i=input
# r=range
# for t in r(1,int(i())+1):
#     v=[0]*200
#     for _ in r(int(i())):
#         l,u=map(int,i().split())
#         if l>u:l,u=u,l
#         for k in r((l-1)//p2,(u-1)//p2+1):v[k]+=1
#     print('#{} {}'.format(t,max(v)))

# for t in range(1,int(input())+1):
#     n = int(input())# 학생 수
#     st = []
#     for i in range(n):
#         x, y = map(int,input().split()) #현 위치, 갈 위치 , 중복 x
#         x = x//p2 if x%p2 else x//p2-1
#         y = y//p2 if y%p2 else y//p2-1
#         st.append(sorted([x,y]))
#     #몇 스텝만에 이동하나 ?, 동선 겹치면 동시에 이동 불가
#     step = 0 # 마지막 []로 하나 더 더함
#     st.sort(key = lambda x: (x[1],x[0]) )
#     while st:
#         temp = [st[0]]
#         for i in range(1,len(st)):
#             if st[i][0] >= temp[-1][1]:# 안겹치면 삭제
#                 temp.append(st[i])
#         else:
#             for i in temp:
#                 st.remove(i)
#             step += 1
#     if st:
#         step += 1
#     print(f'#{t} {step}')