#%%
"""
7
1 1 5 5
1111111
1111101
1000101
1011101
1000001
1111111
1000001
"""

#%%
def find_way_from_maze(r, c):
    visited[r][c] = True
    if (r,c) == (ex, ey): return True
    #동쪽
    if M[r][c+1] == '0' and visited[r][c+1]==False:
        if find_way_from_maze(r, c+1):
            M[r][c+1] = trace
            return True
    #남쪽
    if M[r+1][c] == '0' and visited[r+1][c]==False:
        if find_way_from_maze(r+1, c):
            M[r+1][c] = trace
            return True
    #서쪽
    if M[r][c-1] == '0' and visited[r][c-1]==False:
        if find_way_from_maze(r, c-1):
            M[r][c-1] = trace
            return True
    #북쪽
    if M[r-1][c] == '0' and visited[r-1][c]==False:
        if find_way_from_maze(r-1, c):
            M[r-1][c] = trace
            return True
    return False
#%%
trace = '\u00B7'
n = 7
sx, sy, ex, ey = (int(x) for x in '1 1 5 5'.split())
M = []
# for i in range(n):
#     M.append([c for c in input()])
M = [
    ['1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','1'],
    ['1','1','1','1','1','0','1'],
    ['1','0','0','0','1','0','1'],
    ['1','0','1','1','1','0','1'],
    ['1','0','0','0','0','0','1'],
    ['1','1','1','1','1','1','1']
]

#%%
# row 0 and n+1 are all 1's
# col 0 and n+1 are all 1's
visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
M[ex][ey] = 'e'


if success:
    for row in M:
        for c in row:
            if c == '1':
                print('#', end="")
            elif c == '0':
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")

# %%
