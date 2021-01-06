#%%
import math
INF = math.inf

# 노드, 간선 갯수
n ,m  = 4,7
# 2차원 dp 테이블을 만들고 모든 값을 INF 로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for row in range(1, n+1):
    for col in range(1, n+1):
        if col == row:
            graph[row][col] = 0

# 각 간선의 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
# %%
""" 플로이드 알고리즘 수행 """
for k in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            graph[row][col] = min(graph[row][col], graph[row][k]+ graph[k][col])

# %%
""" 결과 출력 """
for row in range(1 , n+1):
    for col in range(1, n+1):
        if graph[row][col] == INF:
            print("INFINITY", end= ' ')
        else:
            print(graph[row][col], end=' ')

    print()

# %%
