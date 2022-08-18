def selection_sort(x,n):
        if not isinstance(x,list):
            x = list(x)
        if n > len(x):
            print(f"change value of n: {n} to {len(x)} for fixing error")
            n = len(x)
        elif n < 0:
            print(f"change value of n: {n} to 0 for fixing error")
            n = 0

        for i in range(n):
            min_idx = i
            for k in range(i+1,len(x)):
                if x[min_idx] > x[k]:# 마지막까지 돌면서 최소를 찾아야함
                    min_idx = k
            x[min_idx] , x[i] = x[i], x[min_idx]
        return x


x = [10,9,8,7,6,5,4,3,2,1]

print(selection_sort(x,-10)) # 정렬해서 앞으로 가져올 요소의 수를 정할 수 있다.
