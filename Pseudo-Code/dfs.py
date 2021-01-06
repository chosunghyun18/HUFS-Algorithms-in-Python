# %%
graph = [
    [],
    [2,3],#a
    [1,3,5, 8], #b
    [1, 2, 4], #c
    [3,6], #d
    [2,7], #e
    [4],#f
    [5],#g
    [2] #f
]
start = 1
curr_time = 1
pre = [0] * len(graph)
post = [0] * len(graph)
visited = [False] * len(graph)
parent = [None] * len(graph)

# %%
""" Recursive DFS """


def dfs(v):
    global curr_time
    visited[v] = True
    pre[v] = curr_time
    curr_time +=1
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)
    post[v] = curr_time
    curr_time +=1

stack =[]
dfs(start)

# %%
""" Iteration DFS """

def dfs_iter(start):
    stack.append((None, start))
    while stack:
        p, now = stack.pop()
        if not visited[now]:
            visited[now] =True
            parent[now] = p
            print(now, end=' ')
            for i in graph[now]:
                if not visited[i]:
                    stack.append((now, i))

stack =[]
visited = [False] * len(graph)
dfs_iter(start)
# %%
