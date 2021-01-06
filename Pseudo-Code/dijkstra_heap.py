#%%
import sys, math, heapq
# input = sys.stdin.readline
INF = math.inf

# 노드의 갯수, 간선의 갯수
n, m = 6, 11

#시작 노드
# start = int(input())
start = 1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#%%
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q) # dist: 햔재 노드에서 weight, now: 현재노드
        if dist > distance[now]:
            continue
        for n, w in graph[now]:
            cost = w + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

dijkstra(start)
# %%
print("INFINITY") if INF in distance[1:] else print(distance[1:])
# %%
