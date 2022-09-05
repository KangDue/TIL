import sys
sys.stdin = open('input.txt')
import sys
read = sys.stdin.readline
text = read().rstrip()
temp = [0]*26
for i in range(26):
    temp[i]=text.find(chr(97+i))
print(*temp)
