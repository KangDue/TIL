import sys
sys.stdin = open('input.txt',encoding='utf-8')

import re # re 안써져 ...
for t in range(1, int(input())+1):
    n = int(input())
    text = input()
    stext = []
    start = 0
    for i in range(len(text)): #문장 분리
        if text[i] in ["?",".","!"]:
            stext.append(text[start:i])
            start = i+1
    c = [0]*len(stext)
    for i in range(len(stext)): #각 문장
        temp = stext[i].split()
        for k in temp:# 각 단어
            if k[0].isupper():
                if len(k) == 1: #한글자 짜리 대문자
                    c[i] += 1
                else: #끝이 아니라 나머지 전부...
                    for z in range(1,len(k)):
                        if not k[z].islower():
                            break
                    else:
                        c[i] += 1
    print(f'#{t}',*c)