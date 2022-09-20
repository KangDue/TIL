import sys
sys.stdin = open('input.txt')
"""
16진수를 2진수로 각 4자리씩 이어붙여라
"""
from itertools import combinations as cb
from math import pow,isclose
nums = [pow(2,-i) for i in range(1,13)]
for t in range(int(input())):
    flag=True
    f = float(input())
    for i in range(1,13):#범위 잘 보자
        for c in cb(nums,i):
            temp = sum(c)
            if isclose(temp,f):break
        if isclose(temp,f):break
    else: flag = False
    if flag:
        ans = ['0']*12
        for i in c:
            ans[nums.index(i)]='1'
        ans = ''.join(ans)
        ans = ans[:ans.rindex('1')+1]
    else:ans = 'overflow'
    print(f'#{t+1} {ans}')

# import struct
# def binary(num):
#     return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
#! = big - endian 으로 나타내라는 뜻
#f = float 형태를 받아온다는 뜻
#struct.pack을 통해 받은 값을 32bit(4byte) 로 가져와서 길이 4인 리스트를 줌.
# print(binary(0.125))
# print(struct.pack('!f', 0.5))
# print(struct.pack('!d', 0.5))
#
# # step 1.
# for i in struct.pack('!f', 0.5):
#     print(i)
"""
0.5의 IEEE-754표기는 
32bit 표기 00111111 00000000 00000000 00000000 
10진수 -> 64 0 0 0 으로 나타난다. 
"""

