""""
포켓몬마스터 다솜이
N,M = 도감의 포켓몬 수 ,맞출 문제 수
둘째줄 부터 1~N번까지 포켓몬 이름 (첫글자만 대문자, 나머지 소문자)
그다음 M개의 줄은 맞출 문제
도감번호를 주면 포켓몬 이름을, 포켓몬 이름을 주면 도감 번호를
출력하자!
"""
o = open('input.txt')
n,m = map(int,next(o).split())
pokedex = {str(i+1):next(o).rstrip() for i in range(n)}
pokename = {pokedex[i]:i for i in pokedex}
for i in o:
    temp = i.rstrip()
    print(pokedex.get(temp) or pokename.get(temp))