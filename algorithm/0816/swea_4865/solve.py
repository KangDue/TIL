import sys
sys.stdin = open('input.txt',encoding='utf-8')

#문자열 a, b를 받고 a의 문자중 b에 가장 많은 글자 수 출력
for t in range(1,int(input())+1):
    a, b = list(set(input())), input()
    print(f'#{t} {max([b.count(i) for i in a])}') #b에서 a문자별 갯수 리스트 만들고 max값