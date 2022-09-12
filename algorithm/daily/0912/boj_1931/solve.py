"""
회의실 배정
greedy하게 가봅시다!
아주 대표적인 greedy 문제
시작시간도 고려를 해야함.
1 1
3 3
1 3 의 경우 3개지만, 끝나는 시간으로만 정렬하면
1 1 , 3 3 두 회의밖에 못함.
시작시간 고려시
1 1, 1 3, 3 3 의 3개 정상적으로 가능
"""
o=open('input.txt');next(o);a=e=0
for x,y in sorted(map(lambda x:[*map(int,x.split())],o),key=lambda x:x[::-1]):
    if x>=e:a+=1;e=y
print(a)