def permu(x,n):
    for i in range(len(x)):
        if n == 1:
            yield [x[i]]
        else:
            for e in permu(x[i+1:],n-1): # 그냥 x쓰면 중복 순열, x[:i]+x[i+1:] 순열
                yield [x[i]] + e               # x[i:] 쓰면 중복 조합, x[i+1:] 쓰면 조합
for i in permu([1,2,3,4],3):
    print(i)

n, k = 5, 3
count = 0

def DFS(sums, answer): # 재귀를 잘 쓰자. ㅠㅠ
    global count
    if sums > n: # n보다 합이 크면 밴
        return None
    if n == sums:
        print(answer[:-1])
        count += 1
        if count == k:
            return None
    for i in (1,2,3): #
        DFS(sums+i, answer + str(i) + '+')

DFS(0,"")


# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr): # 정렬이 안됨. 뭐시기 종소리 형태
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result