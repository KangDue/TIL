import sys
sys.stdin = open('input.txt')
# for t in range(1,int(input())+1):
#     text,pattern = input().split()
#     lp = len(pattern)
#     c = 0
#     while 1:
#         a = text.find(pattern)
#         if a > -1:
#             text = text[:a]+text[a+lp:]
#             c += 1
#         else:
#             break
#     ans = c + len(text)
#     print(f'#{t} {ans}')

for t in range(1,int(input())+1):
    text,pattern = input().split() #전체길이 - 패턴이차치하는길이 + 패턴 수
    ans = len(text) - text.count(pattern) * ( len(pattern) -1)
    print(f'#{t} {ans}')