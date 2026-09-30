INF = 1 << 30
sys.setrecursionlimit(200_000)

n, m = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    v, u = map(int, input().split()); v -= 1; u -= 1
    edges[v].append(u)

vis = [False] * n
finish = [False] * n
reachable_min = [INF] * n
scc = []
stack = []
def dfs(x):
    global idx
    og_idx = idx
    stack.append(x)
    reachable_min[x] = idx
    for i in edges[x]:
        if not vis[i]:
            vis[i] = True
            idx += 1
            reachable_min[x] = min(reachable_min[x], dfs(i))
        else:
            if not finish[i]:
                reachable_min[x] = min(reachable_min[x], reachable_min[i])
    if og_idx == reachable_min[x]:
        t = -1
        vl = []
        while x != t:
            t = stack.pop()
            finish[t] = True
            vl.append(t)
        scc.append(vl)
    return reachable_min[x]

for i in range(n):
    if not vis[i]:
        vis[i] = True
        stack = []
        idx = 0
        dfs(i)