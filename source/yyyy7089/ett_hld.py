sys.setrecursionlimit(110000)

# Copypaste Segtree Class Here

n = int(input())
edges = [dict() for i in range(n)]
raw_edges = []
for i in range(n-1):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    edges[a][b] = w
    edges[b][a] = w
    raw_edges.append((a, b))

root = 0
vis = [False] * n; vis[root] = True
parent = [-1] * n
main_child = [-1] * n
depths = [0] * n
def dfs(x):
    tot = 1
    ms = 0; mi = -1
    for j in edges[x]:
        if not vis[j]:
            vis[j] = True
            depths[j] = depths[x] + 1
            parent[j] = x
            rv = dfs(j)
            tot += rv
            if rv > ms:
                ms = rv
                mi = j
    main_child[x] = mi
    return tot
dfs(root)

for i in range(n-1):
    if parent[raw_edges[i][0]] == raw_edges[i][1]:
        raw_edges[i] = raw_edges[i][0]
    else:
        raw_edges[i] = raw_edges[i][1]

sparse_table = [parent[:]]
for i in range(20):
    ns = []
    for j in range(n):
        if sparse_table[i][j] == -1:
            ns.append(-1)
        else:
            ns.append(sparse_table[i][sparse_table[i][j]])
    sparse_table.append(ns)

def up(x, n):
    for i in range(20):
        if (n >> i) & 1:
            x = sparse_table[i][x]
    return x

def lca(x1, x2):
    dx1 = depths[x1]
    dx2 = depths[x2]
    if dx1 < dx2:
        x2 = up(x2, dx2 - dx1)
    if dx1 > dx2:
        x1 = up(x1, dx1 - dx2)
    for move in range(19, -1, -1):
        if sparse_table[move][x1] != sparse_table[move][x2]:
            x1 = sparse_table[move][x1]
            x2 = sparse_table[move][x2]
    if x1 == x2:
        return x1
    return parent[x1]

idx = 0
hld = []
hldidxl = [-1] * n
hldposl = [-1] * n

vis = [False] * n; vis[root] = True
def dfs2(x):
    global idx
    u = []
    e = x

    while x != -1:
        vis[x] = True
        hldidxl[x] = idx
        hldposl[x] = len(u)
        u.append(x)
        x = main_child[x]

    su = segtree(len(u))
    for i in range(len(u)):
        if u[i] == root:
            continue
        su.set(i, edges[parent[u[i]]][u[i]])
    su.init()

    hld.append((parent[e], su))

    for i in u:
        for j in edges[i]:
            if not vis[j]:
                idx += 1
                dfs2(j)
dfs2(root)

for i in range(int(input())):
    q, *ql = map(int, input().split())
    if q == 1:
        i = raw_edges[ql[0]-1]
        hld[hldidxl[i]][1].update(hldposl[i], ql[1])
    if q == 2:
        mv = 0

        c1 = ql[0] - 1
        c2 = ql[1] - 1
        lc = lca(c1, c2)

        while True:
            if hldidxl[c1] == hldidxl[lc]:
                if c1 == lc:
                    break
                mv = max(mv, hld[hldidxl[c1]][1].query(hldposl[lc] + 1, hldposl[c1]))
                break
            mv = max(mv, hld[hldidxl[c1]][1].query(0, hldposl[c1]))
            c1 = hld[hldidxl[c1]][0]

        while True:
            if hldidxl[c2] == hldidxl[lc]:
                if c2 == lc:
                    break
                mv = max(mv, hld[hldidxl[c2]][1].query(hldposl[lc] + 1, hldposl[c2]))
                break
            mv = max(mv, hld[hldidxl[c2]][1].query(0, hldposl[c2]))
            c2 = hld[hldidxl[c2]][0]

        print(mv)