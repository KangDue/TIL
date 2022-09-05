import sys
sys.stdin = open('input.txt')
a,=map(int,input().split()) #컴마를 붙여주면 튜플 내용처럼 받을 수 있다. 안그러면 map 그 자체 받아옴
if a > 89:print("A")
elif a>79:print("B")
elif a>69:print("C")
elif a>59:print("D")
else: print("F")