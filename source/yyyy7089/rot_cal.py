q = convex_hull(l)

lg = len(q)
md = -1
i = 0; j = 1
while i <= lg:
    md = max(md, (q[i%lg].x-q[j%lg].x) ** 2 + (q[i%lg].y-q[j%lg].y) ** 2)
    c = ccw(q[i%lg], q[(i+1)%lg], q[(i+1)%lg] + q[(j+1)%lg] - q[j%lg])
    if c > 0:
        j += 1
    else:
        i += 1
print(math.sqrt(md))