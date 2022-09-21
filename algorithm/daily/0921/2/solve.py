import sys
sys.stdin = open('input.txt')
"""
6자리 숫자에 대해 완전검색을 활용하여
baby-gin 해결해보자
2개의 트리플렛(같은 숫자)
2개의 런 (연속된 숫자) 면 1
아니면 0
"""
# num  문자열 형태
# brute force로 본다는건 baby gin인 모든 경우의 수를 본다는 이야기 ???
import sys
find = 0
def bglist(nums='0123456789',case='',mine = '111123'): #판별할 숫자, 깊이, 런 트리플렛 카운트
    global find
    if len(case)==6:
        if case == mine: find=1;return 1
    elif find == 0:
        for i in range(10):
            bglist(nums,case+nums[i]*3)
            if i<=7:
                bglist(nums,case+nums[i:i+3])
bglist()
print(find)