import sys
sys.stdin = open('input.txt')

import sys
read = sys.stdin.readline
st = list(range(1,31))
for i in range(28):
    st.remove(int(read().rstrip()))
print(*st,sep='\n')