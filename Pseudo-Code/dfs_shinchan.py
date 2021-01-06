# %%
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2, 6, 8],
    [1,7]
]
start = 1


# %%
""" Recursive DFS """


def dfs_recur(v):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_recur(i)

stack =[]
visited = [False] * len(graph)
dfs_recur(start)
# %%
""" Iteration DFS """

def dfs_iter(start):
    stack.append(start)
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] =True
            print(now, end=' ')
            for i in graph[now]:
                if not visited[i]:
                    stack.append(i)

stack =[]
visited = [False] * len(graph)
dfs_iter(start)

# %%
