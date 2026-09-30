INF = 1 << 60
EPS = 10 ** (-6)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        else:
            return Point(other * self.x, other * self.y)

    def __matmul__(self, other):
        return self.x * other.y - self.y * other.x

    def __truediv__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return -INF
            else:
                return INF
        else:
            return (other.y - self.y) / (other.x - self.x)

    def __pow__(self, other):
        return abs(self.x) ** other + abs(self.y) ** other

    def __abs__(self):
        return pow(self, 2) ** (1 / 2)

    def __str__(self):
        return ' '.join((str(self.x), str(self.y)))

    def __hash__(self):
        return (self.x, self.y).__hash__()

origin = Point(0, 0)

def ccw(p1: Point, p2: Point, p3: Point):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def ccw_a(p1, p2, p3):
    return sgn(ccw(p1, p2, p3))

def sgn(v):
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0

def cross(d1, d2, d3, d4):
    x1, y1 = d1.x, d1.y
    x2, y2 = d2.x, d2.y
    x3, y3 = d3.x, d3.y
    x4, y4 = d4.x, d4.y
    if (-EPS <= ccw_a(d1, d2, d3) <= EPS and min(x1,x2) - EPS <= x3 <= max(x1,x2) + EPS and min(y1,y2) - EPS <= y3 <= max(y1,y2) + EPS) or\
       (-EPS <= ccw_a(d1, d2, d4) <= EPS and min(x1,x2) - EPS <= x4 <= max(x1,x2) + EPS and min(y1,y2) - EPS <= y4 <= max(y1,y2) + EPS) or\
       (-EPS <= ccw_a(d3, d4, d1) <= EPS and min(x3,x4) - EPS <= x1 <= max(x3,x4) + EPS and min(y3,y4) - EPS <= y1 <= max(y3,y4) + EPS) or\
       (-EPS <= ccw_a(d3, d4, d2) <= EPS and min(x3,x4) - EPS <= x2 <= max(x3,x4) + EPS and min(y3,y4) - EPS <= y2 <= max(y3,y4) + EPS):
        return True
    elif -EPS <= ccw_a(d1, d2, d3) - ccw_a(d1, d2, d4) <= EPS or -EPS <= ccw_a(d3, d4, d1) - ccw_a(d3, d4, d2) <= EPS:
        return False
    else:
        return True

def line_cross_dist(p1, p2, p3, p4):
    if cross(p1, p2, p3, p4):
        diff1 = p2-p1
        diff2 = p4-p3
        if diff2.x == 0:
            x = p3.x
            a = diff1.y / diff1.x
            b = p1.y - a * p1.x
            y = a * x + b
            pt = Point(x, y)
            return abs(p1-pt), pt
        else:
            a1 = diff1.y / diff1.x
            b1 = p1.y - a1 * p1.x
            a2 = diff2.y / diff2.x
            b2 = p3.y - a2 * p3.x
            x = (b2-b1) / (a1-a2)
            y = a1 * x + b1
            pt = Point(x, y)
            return abs(p1-pt), pt
    return INF, Point(-1, -1)

def sort_order_1(e):
    Pt1 = e[0] - light
    typ = e[2]
    if -EPS < Pt1.x < EPS: Pt1.x = 0
    if -EPS < Pt1.y < EPS: Pt1.y = 0
    v1 = [6,5,4,7,0,3,8,1,2][sgn(Pt1.x)*3+sgn(Pt1.y)+4]
    if typ == 2:
        ue = -abs(Pt1)
    else:
        ue = abs(Pt1)
    if typ == 0:
        typ = 1.5
    return (v1, round(float(Pt1/origin), 7), typ, ue)

def polygon_area(pts):
    a = 0
    lg = len(pts)
    for i in range(lg):
        a += pts[i] @ pts[(i+1)%lg]
    return abs(a/2)

n, m = map(int, input().split())
l = [input().strip() for i in range(n)]

id_ = 0
box_lines = []
box_dots = []
light_i = -1
for i in range(n):
    for j in range(m):
        if l[i][j] == '*':
            light = Point(j+0.5, i+0.5)
            light_i = i
        if l[i][j] == '#':
            box_lines_t = []
            box_lines_t.append((Point(j, i), Point(j, i+1)))
            box_lines_t.append((Point(j, i+1), Point(j+1, i+1)))
            box_lines_t.append((Point(j+1, i+1), Point(j+1, i)))
            box_lines_t.append((Point(j+1, i), Point(j, i)))
            box_lines.append(box_lines_t)
            if i == light_i:
                box_dots.append((Point(j, i), id_, 1))
                box_dots.append((Point(j, i+1), id_, 1))
                box_dots.append((Point(j+1, i+1), id_, 1))
                box_dots.append((Point(j+1, i), id_, 1))
            else:
                box_dots.append((Point(j, i), id_, 0))
                box_dots.append((Point(j, i+1), id_, 0))
                box_dots.append((Point(j+1, i+1), id_, 0))
                box_dots.append((Point(j+1, i), id_, 0))
            id_ += 1
box_dots = sorted(box_dots, key = sort_order_1)

found_dots = [0] * id_
sweep_dots = [] # 0: 자기만 확인, 1: inner->outer, 2: outer->inner
box_angles = [set() for i in range(id_ + 1)]
for i, j, k in box_dots:
    found_dots[j] += 1
    d = abs(light-i)
    md = d
    for l in box_lines[j]:
        md = min(md, line_cross_dist(light, i, l[0], l[1])[0])
    if md + EPS >= d:
        if k == 0 and found_dots[j] == 1:
            sweep_dots.append((i, j, 2))
            box_angles[j].add(round(light/i, 7))
        elif k == 0 and found_dots[j] == 4:
            sweep_dots.append((i, j, 1))
            box_angles[j].add(round(light/i, 7))
        elif k == 1 and found_dots[j] == 2:
            sweep_dots.append((i, j, 1))
            box_angles[j].add(round(light/i, 7))
        elif k == 1 and found_dots[j] == 3:
            sweep_dots.append((i, j, 2))
            box_angles[j].add(round(light/i, 7))
        else:
            sweep_dots.append((i, j, 0))
sweep_dots.append((Point(0, 0), id_, 0))
sweep_dots.append((Point(m, 0), id_, 0))
sweep_dots.append((Point(m, n), id_, 0))
sweep_dots.append((Point(0, n), id_, 0))
sweep_dots = sorted(sweep_dots, key = sort_order_1)

frame = []
frame.append((Point(0, 0), Point(m, 0)))
frame.append((Point(m, 0), Point(m, n)))
frame.append((Point(m, n), Point(0, n)))
frame.append((Point(0, n), Point(0, 0)))
box_lines.append(frame)
line_amt = len(box_lines)

final_dots = []
for pt, box_id, typ in sweep_dots:
    angle = round(light/pt, 7)
    if typ == 0:
        d = abs(light-pt)
        flag = False
        for j in range(line_amt):
            for k1, k2 in box_lines[j]:
                if line_cross_dist(light, pt, k1, k2)[0] + EPS < d:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            final_dots.append(pt)
    elif typ == 1:
        d = abs(light-pt)
        pt_extend = light + (pt-light) * 1000
        md = INF
        md_pt = Point(-1, -1)
        for j in range(line_amt):
            if angle in box_angles[j]:
                continue
            for k1, k2 in box_lines[j]:
                dd, dd_pt = line_cross_dist(light, pt_extend, k1, k2)
                if dd < md:
                    md = dd
                    md_pt = dd_pt
        if md >= d - EPS:
            final_dots.append(pt)
            final_dots.append(md_pt)
    elif typ == 2:
        d = abs(light-pt)
        pt_extend = light + (pt-light) * 1000
        md = INF
        md_pt = Point(-1, -1)
        for j in range(line_amt):
            if angle in box_angles[j]:
                continue
            for k1, k2 in box_lines[j]:
                dd, dd_pt = line_cross_dist(light, pt_extend, k1, k2)
                if dd < md:
                    md = dd
                    md_pt = dd_pt
        if md >= d - EPS:
            final_dots.append(md_pt)
            final_dots.append(pt)

final_area = polygon_area(final_dots)
print(n*m - id_ - final_area)