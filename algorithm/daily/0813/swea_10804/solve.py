import sys
sys.stdin = open('input.txt', encoding='utf-8')

# answers = []
# for t in range(1,int(input())+1):
#     info = list(input().split())
#     robot = {'O': [1, 0], 'B': [1, 0]}
#     n = int(info[0]) # 누를 버튼의 수
#     second = 0
#     for i in range(1,n*2+1,2): # 명령줄의 길이는 2 * ln
#         obj = info[i] # n을 따로 처리하지않고 두칸씩 obj는 로봇 명
#         button = int(info[i+1]) #버튼 있는 위치
#         dist = abs(button - robot[obj][0]) # 로봇 현위치부터 버튼까지 거리
#         robot_s = second - robot[obj][1] # 어느 로봇이 이동하는데 걸리는 시간, f
#         second += 1 if dist <= robot_s else (dist - robot_s + 1)# else는 이동 후 버튼누르는 시간
#         robot[obj] = [button,second] #로봇 위치를 버튼 위치로 갱신, # 로봇의 시간을 현재 시간으로 갱신
#     answers.append(f'#{t} {second}')
# print(*answers,sep="\n")

# answers = [] #나중에 다시 풀어본 것
# for t in range(1, int(input())+1):
#     order = input().split()
#     n = int(order[0])
#     robot = {'O':[1, 0], 'B':[1, 0]}# start at 1 [position, time]
#     step = 0
#     for i in range(1, n*2, 2):
#         name,button = order[i],int(order[i+1])
#         distance = abs( button - robot[name][0] )
#         own_step = step - robot[name][1] #처음엔 무조건 음수일테니 첫 녀석의 step으로 초기화
#         step += 1 if distance <= own_step else (distance - own_step + 1)
#         """
#         distance가 앞서 움직인 녀석이 움직이는 동안 갈수 있는 거리 이하면 +1, 초과면 그 차이 + 버튼 누르는 step 까지
#         why +1이냐 ? 버튼 누르는 step +1 한것임. (무조건 버튼 누르기 기준으로 생각)
#         """
#         robot[name] = [button,step]
#     answers.append(f'#{t} {step}')
# print(*answers,sep="\n")

#코드 길이 줄이기용
a = []
for t in range(1, int(input())+1):
    o = input().split()
    n = int(o[0])
    r = {'O':[1, 0], 'B':[1, 0]}
    w = 0
    for i in range(1, n*2, 2):
        q,b = o[i],int(o[i+1])
        d = abs( b - r[q][0] )
        p = w - r[q][1]
        w += 1 if d <= p else (d - p + 1)
        r[q] = [b,w]
    a.append(f'#{t} {w}')
print(*a,sep="\n")



"""너무 시간낭비해서 .. 일단 하고 나중에 다시풀기"""
# for t in range(1, int(input())+1): #첫 시도 시간초과
#     direct = input().split()
#     n,root = int(direct[0]), direct[1:]
#     orange,blue = [0]*101, [0]*101
#     root = [( root[i],int(root[i+1]) ) for i in range(0,len(root),2)]
#     for i in root:
#         if i[0] == 'O':
#             orange[i[1]]=1
#         else:
#             blue[i[1]]=1
#     count, step = 0,0
#     robot = {'O' : 1, 'B' : 1}
#     while count != len(root):
#         o,b = 1,1
#         if orange[robot['O']] == 1:
#             if root[count][0] == 'O':
#                 o = 0
#                 count += 1
#                 step += 1
#                 orange[robot['O']] = 0 #버튼 누르면서 한스텝 더 소모
#                 if blue[robot['B']] != 1 and robot['B'] <100 :
#                     robot['B'] += 1
#                 continue
#         else:
#             if robot['O'] < 100 and 1 in orange:
#                 step += orange.index(1) - robot['O']
#                 robot['O'] = orange.index(1)
#                 print(root[count], step, robot)
#
#
#
#         if blue[robot['B']] == 1:
#             if root[count][0] == 'B':
#                 b = 0
#                 count += 1
#                 step += 1
#                 blue[robot['B']] = 0
#                 continue # 버튼 누르면 한턴 소모 된거임
#         else: # 둘 다 버튼 안누를 때
#             if robot['B'] < 100 and 1 in blue:
#                 step += blue.index(1) - robot['B']
#                 robot['B'] = blue.index(1)
#                 print(root[count], step, robot)
#
#         if o*b:
#             step += 0
#     answers.append(f'#{t} {step}')
# print(*answers, sep="\n")









    # b_job = 0
    # o_job = 0

    # while count != n:
    #     try:
    #         if mode:
    #             step += abs(blue_jobs[b_job][1] - robot['B']) + 1  # 이동 + 누르는 시간
    #             robot['B'] = blue_jobs[b_job][1]
    #             count += 1
    #             if orange_jobs[o_job:] : #끝이 아니면
    #                 if orange_jobs[o_job][1] <= blue_jobs[b_job][1]: #오렌지 녀석 미리 이동
    #                     robot['O'] = orange_jobs[o_job][1]
    #                 else:
    #                     max_pos = robot['O'] + abs(blue_jobs[b_job][1] - robot['B']) + 1
    #                     if max_pos > orange_jobs[o_job][1]:
    #                         robot['O'] =  orange_jobs[o_job][1]
    #                     else:
    #                         robot['O'] += abs(blue_jobs[b_job][1] - robot['B']) + 1
    #             else:
    #                 pass
    #             if next(check)[0] == 'B':
    #                 pass
    #             else:
    #                 mode = not mode
    #             print(blue_jobs[b_job], orange_jobs[o_job])
    #             b_job += 1
    #         else:
    #             step += abs(orange_jobs[o_job][1] - robot['O']) + 1  # 이동 + 누르는 시간
    #             robot['O'] = orange_jobs[o_job][1]
    #             count += 1
    #             if blue_jobs[b_job:] : #블루 일이 끝이 아니면
    #                 if blue_jobs[b_job][1] <= orange_jobs[o_job][1]: #블루 녀석 미리 이동
    #                     robot['B'] = blue_jobs[b_job][1]
    #                 else:
    #                     max_pos = robot['B'] + abs(orange_jobs[o_job][1] - robot['O']) + 1
    #                     if max_pos > blue_jobs[b_job][1]:
    #                         robot['B'] =  blue_jobs[b_job][1]
    #                     else:
    #                         robot['B'] += abs(orange_jobs[o_job][1] - robot['O']) + 1
    #             else:
    #                 pass
    #
    #             if next(check)[0] == 'O':
    #                 pass
    #             else:
    #                 mode = not mode
    #             print(blue_jobs[b_job], orange_jobs[o_job])
    #             o_job += 1
    #     except:
    #         break
