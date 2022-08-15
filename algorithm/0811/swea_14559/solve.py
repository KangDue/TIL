import sys
sys.stdin = open('input.txt')
def cart(arr1,arr2):
    temp = {i:[] for i in arr1}
    for i in arr1:
        for j in arr2:
            temp[i].append(j)
    return temp

T = int(input())
for t in range(1,T+1):
    n,start,end = map(int,input().split())
    m = int(input())
    array = [ list(map(int,input().split())) for i in range(m)]
    #dict의 형태보단 matrix가 좋을것 같았는데 mat가 너무 크다.
    