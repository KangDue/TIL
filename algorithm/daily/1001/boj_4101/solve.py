o = open('input.txt')
for i in o:
    a,b=map(int,i.split())
    if (a,b)==(0,0):
        break
    print('Yes') if a > b else print('No')