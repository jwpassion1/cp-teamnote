from collections import deque
INF = 1 << 63

N, P = map(int, input().split())

V = N  # system size
connect = [[] for _ in range(V)]
flow = [{} for _ in range(V)]
capacity = [{} for _ in range(V)]


def add_edge(u, v, cap):
    connect[u].append(v)
    flow[u][v] = 0
    capacity[u][v] = cap


for _ in range(P):
    u, v = map(int, input().split())
    add_edge(u - 1, v - 1, 1)
    add_edge(v - 1, u - 1, 0)

source, sink = 0, 1
net_flow = 0


def bfs():
    level[:] = [-1] * V
    level[source] = 0
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in connect[u]:
            if capacity[u][v] - flow[u][v] > 0 > level[v]:
                queue.append(v)
                level[v] = level[u] + 1
    return level[sink] >= 0


def dfs(u, max_flow):
    if u == sink:
        return max_flow
    try:
        while True:
            v = next(it[u])
            if level[v] == level[u] + 1 and capacity[u][v] > flow[u][v]:
                flow_change = dfs(v, min(capacity[u][v] - flow[u][v], max_flow))
                if flow_change > 0:
                    flow[u][v] += flow_change
                    flow[v][u] -= flow_change
                    return flow_change
    except StopIteration:
        return 0


level = [-1] * V
while bfs():
    it = [*map(iter, connect)]
    while True:
        flow_change = dfs(source, INF)
        if flow_change == 0:
            break
        net_flow += flow_change

print(net_flow)