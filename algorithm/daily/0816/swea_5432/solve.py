import sys
sys.stdin = open('input.txt', encoding='utf-8')
# for t in range(1,int(input())+1):
#     pipe = list(input())
#     lp = len(pipe)
#     for i in range(lp-1):
#         if (pipe[i], pipe[i+1]) == ('(',')'):
#             pipe[i] = '1'
#             pipe[i+1] = 0
#     ans = 0
#     for i in range(lp-1):
#         if pipe[i] == '(':
#             idx = pipe[i+1:].index(')')
#             ans += pipe[ i+1 : i + 1 + idx ].count('1')+1
#             pipe[i+1+idx] = 0
#     print(f'#{t} {ans}')


for t in range(int(input())):
    layer=on=piece=0
    for i in input():
        j=i<')' #철근이 start or not
        layer+=2*j-1 #철근 겹치기, 철근 끝나면 -1 함.
        piece+=(j or layer)*on #뒤가 닫는 괄호가 아니면 계속 1씩 더함. 레이저로 가르는 순간  쌓인 겹만큼 더한다.
        on=j #철근이 끝나기 전인 상태인가?
    print(f'#{t+1}',piece)


"""
()= 1칸, 

"""