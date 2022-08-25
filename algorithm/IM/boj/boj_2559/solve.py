import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
온도의 수열이 주어질때 연속적인 몇일간 합이 max인 경우
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n,k=map(int,sr().split())#온도 개수, k일간 연속
    temperature = [*map(int,sr().split())]
    #연속적인 숫자를 더할때 겹치는 부분때문에 속도가 느린가?
    #양 끝 값만 건드려 볼끼??
    #print(max(map(lambda x: sum(temperature[x:x+k]),range(n-k+1))))
    start = sum(temperature[:k])#초기값.
    maxv = start
    for i in range(1,n-k+1):
        start = start + temperature[i+k-1] - temperature[i-1]
        if maxv < start: maxv = start
    if maxv < start: maxv = start
    print(maxv)
