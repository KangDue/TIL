import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    answer = input()
    score = 0
    temp = 0
    for i in answer:
        if i=='O':
            temp += 1
        else:
            temp = 0
        score += temp
    print(score)