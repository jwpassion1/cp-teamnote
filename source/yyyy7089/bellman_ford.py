INF = 1 << 30
v, e = map(int, input().split())
graph = [[] for i in range(v)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1, c))

dist = [INF for i in range(v)]
dist[0] = 0
prv_cities = [0]
for i in range(v):
    cities = []
    for j in prv_cities:
        for k, l in graph[j]:
            x = dist[j] + l
            if dist[k] > x:
                dist[k] = x
                cities.append(k)
    prv_cities = cities

for j in prv_cities:
    for k, l in graph[j]:
        x = dist[j] + l
        if dist[k] > x:
            print(-1)
            sys.exit()

for i in range(1, v):
    print(dist[i] if dist[i] < INF else -1)