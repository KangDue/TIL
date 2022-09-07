import sys
sys.stdin = open('input.txt')
#단어를 길이순, 사전순 정렬
from collections import defaultdict
word = defaultdict(set)
for i in range(int(input())):
    text = input()
    word[len(text)].add(text)
ans = [sorted(list(word[i])) for i in word.keys()]
ans.sort(key=lambda x:len(x[0]))
print(*sum(ans,start=[]),sep='\n')