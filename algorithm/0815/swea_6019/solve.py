import sys
sys.stdin = open('input.txt',encoding='utf-8')
#
# ans =[]
# for t in range(1, int(input())+1):
#     D, A, B, F = map(int,input().split())
#     a = F*D/(A+B)
#     ans.append(f'#{t} {a}')
# print(*ans,sep='\n')


for t in range(int(input())):
    D, A, B, F = map(int,input().split())
    print(f'#{t+1} {F*D/(A+B)}')