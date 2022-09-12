o = list(open('input.txt'))
o = [*map(lambda x:x.split(),o)]
n,order = o[0], o[1:]
stack = []
func = {'push':stack.append, 'pop':stack.pop}

for i in order:
    if i[0] == 'push':
        func[i[0]](i[1])
    elif i[0] == 'pop':
        if len(stack):
            print(func['pop']())
        else:
            print(-1)
    elif i[0] == 'empty':
        print(+(len(stack) == 0))
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)

