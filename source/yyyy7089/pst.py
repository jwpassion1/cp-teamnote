n = int(input())
l = list(map(int, input().split()))
lg = 1 << math.ceil(math.log2(n))
slg = math.ceil(math.log2(n))

segtree = []
values = []
for i in l:
    values.append(i)
    segtree.append((-1, -1))
for i in range(lg - len(l)):
    values.append(0)
    segtree.append((-1, -1))

for i in range(lg-1):
    segtree.append((i*2, i*2+1))
    values.append(values[i*2] + values[i*2+1])

roots = [lg*2-2]

def query(L, R, x):
    Li = roots[x]; Ri = roots[x]
    depth = 1
    tot = 0
    while depth <= slg:
        if L >> (slg - depth) == R >> (slg - depth):
            if (L >> (slg - depth)) & 1:
                Li = segtree[Li][1]
                Ri = segtree[Ri][1]
            else:
                Li = segtree[Li][0]
                Ri = segtree[Ri][0]
        else:
            if (L >> (slg - depth)) & 1:
                Li = segtree[Li][1]
            else:
                if (L >> (slg - depth)) + 1 != (R >> (slg - depth)):
                    tot += values[segtree[Li][1]]
                Li = segtree[Li][0]
            if (R >> (slg - depth)) & 1:
                if (L >> (slg - depth)) + 1 != (R >> (slg - depth)):
                    tot += values[segtree[Ri][0]]
                Ri = segtree[Ri][1]
            else:
                Ri = segtree[Ri][0]
        depth += 1
    if Li == Ri:
        return tot + values[Li]
    else:
        return tot + values[Ri] + values[Li]

def update(i, x):
    q = []
    idx = roots[-1]
    depth = 1
    while depth <= slg:
        if (i >> (slg - depth)) & 1:
            q.append((0, segtree[idx][0]))
            idx = segtree[idx][1]
        else:
            q.append((1, segtree[idx][1]))
            idx = segtree[idx][0]
        depth += 1

    values.append(x)
    segtree.append((-1, -1))
    while len(q) > 0:
        qb, qi = q.pop()
        x += values[qi]
        values.append(x)
        if qb == 0:
            segtree.append((qi, len(segtree)-1))
        else:
            segtree.append((len(segtree)-1, qi))
    roots.append(len(segtree)-1)

for j in range(int(input())):
    i, *l = map(int, input().split())
    if i == 1:
        update(l[0]-1, l[1])
    elif i == 2:
        print(query(l[1]-1, l[2]-1, l[0]))