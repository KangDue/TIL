import sys
sys.stdin = open('input.txt', encoding='utf-8')
#괄호 판별기
for t in range(1,int(input())+1):
    pair = 0
    for i in  input():
        if pair < 0: # ) 중간에 )개수 초과시 끝
            print(f'#{t} -1')
            break
        pair += 1 if i == '(' else -1
    else:#다 끝나고 짝이 맞는지 점검
        if pair != 0:
            print(f'#{t} -1')
        else:
            print(f'#{t} 1')
