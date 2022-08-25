import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""

"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    width, height = map(int,sr().split()) # 가로길이, 세로길이
    n = int(sr())
    #가로로 자를땐 0 과 번호
    #세로로 자를땐 1과 번호
    cols=[0];rows=[0]
    for _ in range(n):
        kind,point = map(int,sr().split())
        if kind:cols.append(point)
        else: rows.append(point)
    rows.append(height);cols.append(width)
    rows.sort(),cols.sort()
    rows = [rows[i+1]-rows[i] for i in range(len(rows)-1)]
    cols = [cols[i + 1] - cols[i] for i in range(len(cols) - 1)]
    print(max(cols)*max(rows))