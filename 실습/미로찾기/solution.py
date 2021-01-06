#%%
n = 8
trace = '\u00B7'
M = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
sx, sy, ex, ey = 1, 1, 6, 6

# %%
def find_way_from_maze(r, c):
    visited[r][c] = True
    if (r,c) == (ex, ey):
        return True
    #동쪽
    if M[r][c+1] == 0 and visited[r][c+1]==False:
        if find_way_from_maze(r, c+1):
            M[r][c+1] = trace
            return True
    #서쪽
    if M[r][c-1] == 0 and visited[r][c-1]==False:
        if find_way_from_maze(r, c-1):
            M[r][c-1] = trace
            return True
    #남쪽
    if M[r+1][c] == 0 and visited[r+1][c]==False:
        if find_way_from_maze(r+1, c):
            M[r+1][c] = trace
            return True
    #북쪽
    if M[r-1][c] == 0 and visited[r-1][c]==False:
        if find_way_from_maze(r-1, c):
            M[r-1][c] = trace
            return True
    return False
# %%
visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
M[ex][ey] = 'e'


if success:
    for row in M:
        for c in row:
            if c == 1:
                print('#', end="")
            elif c == 0:
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")

# %%
