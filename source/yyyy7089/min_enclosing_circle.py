def get_outer_circle(pt1, pt2, pt3):
    x1, y1, x2, y2, x3, y3 = pt1.x, pt1.y, pt2.x, pt2.y, pt3.x, pt3.y
    x_parent = 2*(x1-x2)*(y3-y2)-2*(x3-x2)*(y1-y2)
    y_parent = -x_parent
    x_child = (x2*x2-x1*x1+y2*y2-y1*y1)*(y3-y2)-(x2*x2-x3*x3+y2*y2-y3*y3)*(y1-y2)
    y_child = (y2*y2-y1*y1+x2*x2-x1*x1)*(x3-x2)-(y2*y2-y3*y3+x2*x2-x3*x3)*(x1-x2)
    outer_center = Point(-x_child/x_parent, -y_child/y_parent)
    dist = abs(pt1-outer_center)
    return outer_center, dist

n = int(input())
points = []
for i in range(n):
    points.append(Point(*map(float, input().split())))
random.shuffle(points)

if n == 1:
    print(points[0].x, points[0].y, 0)
    sys.exit()

c, r = Point(0, 0), 0
for i in range(n):
    if abs(points[i]-c) <= r:
        continue
    c, r = points[i], 0
    for j in range(i):
        if abs(points[j]-c) <= r:
            continue
        c, r = (points[i]+points[j])*0.5, abs(points[i]-points[j])*0.5
        for k in range(j):
            if abs(points[k]-c) <= r:
                continue
            c, r = get_outer_circle(points[i], points[j], points[k])
print(c.x, c.y, r)