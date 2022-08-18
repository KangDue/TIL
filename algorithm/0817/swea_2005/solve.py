import sys
sys.stdin = open('input.txt',encoding='utf-8')

pascal = [None,[1]] # 삼각형 10층까지 미리 만들기
for i in range(2, 10 + 1): #n = 1~10
    pascal.append([1] * i)
    for k in range(1, len(pascal[i - 1])):
        pascal[i][k] = pascal[i - 1][k - 1] + pascal[i - 1][k]

for t in range(1,int(input())+1):
    n = int(input()) # n 층 삼각형 만들기
    print(f'#{t}')
    # 답안용 출력기
    for i in pascal[1:n+1]:
        print(*i)

    # 삼각형 모양 출력기
    maxl = len( str(pascal[n])[1:-1].replace(",","") )
    for i in range(1,n+1): # 삼각형 요소 하나당 한 칸이면 좋은데 그게 아니네 ...
        print(f'{str(pascal[i])[1:-1].replace(",",""):^{maxl}}') #답안이랑 다르지만 이쁘게 출력되도록 변경
