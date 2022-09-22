import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
주사위 쌓기, 한 옆면의 숫자 합의 최댓값 구하기
1. 아래 주사위의 윗면은 윗주사위의 아랫면과 같아야 한다.
p2. 주사위 전개도가 주어진다.
위(A) 옆(BCDE) 아래(F)
3. 각 주사위마다 배치가 다름
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n = int(sr())
    def dicemax(a,b): #i번쨰 주사위의 위가 x 번째 면일때 최댓 값.
        temp = dices[a][:]
        temp[b]=temp[pair[b]]=0
        return max(temp)
    dices = [[*map(int, sr().split())] for i in range(n)]#AF,BD,CE는 마주본다.
    #[0,5],[1,3],[p2,4] mathching
    #최대한 옆면에 6이 오게하고 안되면 5,
    pair = {0:5,1:3,2:4,4:2,3:1,5:0}
    maxv = 0
    for i in range(6): #첫 주사위 따라 위도 다바뀜. #윗면 값 고르기
        ans = 0
        up = dices[0][i]#첫 주사위 윗면
        down = dices[0][pair[i]]#첫 주사위 아랫면
        ans += dicemax(0,i)
        for j in range(1,n):#나머지 주사위
            down = up
            didx = dices[j].index(down)
            uidx = pair[dices[j].index(down)]
            up = dices[j][uidx]
            ans += dicemax(j,uidx)
        if maxv < ans:
            maxv = ans
    print(maxv)
