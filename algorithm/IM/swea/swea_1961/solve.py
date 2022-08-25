import sys
sys.stdin = open('input.txt')

d,w,r,p=int,input,range,print
def rot_print(a, n):
    for i in r(n): # n x n matrix
        for k in r(n):  # 90도
            p(a[-1 - k][i], end="")
        p(end=" ")
        for k in r(n):  # 180도
            p(a[-1 - i][-1 - k], end="")
        p(end=" ")
        for k in r(n):  # 270도
            p(a[k][-1 - i], end="")
        p("")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in r(d(w())):
    n = d(w())
    mat = [list(map(d,w().split())) for i in r(n)]
    p(f"#{t+1}")
    rot_print(mat, n)


# 내함수 축약 숏코딩
# for t in range(int(input())):
#     n=int(input());b=[[*input().split()]for _ in '1'*n];c=[*zip(*b)];print(f'#{t+1}')
#     for i in range(n):print(''.join(c[i][::-1]),''.join(b[::-1][i][::-1]),''.join(c[::-1][i]))