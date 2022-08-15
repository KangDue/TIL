import sys
sys.stdin = open('input.txt',encoding='utf-8')

a = [] # python은 지원 안하지만 00년도인 경우도 고려해야해서 12로만 기준 세우면 안댐.
for t in range(1, int(input())+1):
    date = input()
    f, b = int(date[:2]), int(date[2:])
    ans = ""
    f = 13 if f == 0 else f
    b = 13 if b == 0 else b # 편하게 계산하기위해 미리 변경
    if f > 12 and b > 12:# 둘다 12 범위를 벗어나면
        ans = "NA"
    elif f > 12: #앞만 벗어나면
        ans = "YYMM"
    elif b > 12: #뒤만 벗어나면
        ans = "MMYY"
    else:#둘다 안벗어 나면
        ans = "AMBIGUOUS"
    a.append(f'#{t} {ans}')
print(*a, sep="\n")