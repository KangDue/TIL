import sys
sys.stdin = open('input.txt')
import sys
read = sys.stdin.readline
score = read().rstrip()
idx = '-0+'
if score[0]=='F': ans = 0.0
else: ans = ( 68-ord(score[0]) ) + 0.7 + idx.index(score[1])*0.3
print(round(ans,1))
