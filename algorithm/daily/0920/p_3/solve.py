import sys
sys.stdin = open('input.txt')
d = {
    '001101':'0',
'010011':'1',
'111011':'p2',
'110001':'3',
'100011':'4',
'110111':'5',
'001011':'6',
'111101':'7',
'011001':'8',
'101111':'9',
}
code = '0269FAC9A0'#'0DEC'
ans = ''
for i in code:
    ans+=f'{int(i,16):04b}'
r = []
i = 0
while i < len(ans)-6:
    temp = d.get(ans[i:i+6])
    if temp:
        r.append(temp)
        i+=6
    else: i+= 1
print(*r)
