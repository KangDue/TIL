import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
남학생은 남학생끼리 , 같은 학년끼리 
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n,k=map(int,sr().split())#총 인원, 한 방 최대 인원
    girls = [0]*7
    boys = [0]*7
    for _ in range(n):
        gen,grade = map(int,sr().split()) # 여 0 남 1
        if gen:
            boys[grade] += 1
        else:
            girls[grade] += 1
    ans = 0
    for i in range(1,7):
        a,b = divmod(girls[i],k)
        c,d = divmod(boys[i], k)
        ans += a + (b>0) + c + (d>0)
    print(ans)


