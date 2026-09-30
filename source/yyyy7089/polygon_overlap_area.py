INF = 1 << 63

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

def ccw(p1: Point, p2: Point, p3: Point):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def ccw_a(p1, p2, p3):
    return sgn(ccw(p1, p2, p3))

def sgn(x):
    if x == 0:
        return x
    else:
        return round(x / abs(x))

def cross(d1, d2, d3, d4):
    x1 = d1.x; y1 = d1.y; x2 = d2.x; y2 = d2.y; x3 = d3.x; y3 = d3.y; x4= d4.x; y4 = d4.y
    if (ccw_a(d1, d2, d3) == 0 and min(x1,x2) <= x3 <= max(x1,x2) and min(y1,y2) <= y3 <= max(y1,y2)) or\
       (ccw_a(d1, d2, d4) == 0 and min(x1,x2) <= x4 <= max(x1,x2) and min(y1,y2) <= y4 <= max(y1,y2)) or\
       (ccw_a(d3, d4, d1) == 0 and min(x3,x4) <= x1 <= max(x3,x4) and min(y3,y4) <= y1 <= max(y3,y4)) or\
       (ccw_a(d3, d4, d2) == 0 and min(x3,x4) <= x2 <= max(x3,x4) and min(y3,y4) <= y2 <= max(y3,y4)):
        return True
    elif ccw_a(d1, d2, d3) == ccw_a(d1, d2, d4) or ccw_a(d3, d4, d1) == ccw_a(d3, d4, d2):
        return False
    else:
        return True

def add_dot(p1, p2, p3, p4):
    if cross(p1, p2, p3, p4):
        diff1 = p2-p1
        diff2 = p4-p3
        if diff1.x == 0:
            if diff2.x == 0:
                if p1 == p3:
                    if sgn(diff1.y) == sgn(diff2.y):
                        return
                    else:
                        dots.append(p1)
                elif p1 == p4:
                    if sgn(diff1.y) != sgn(diff2.y):
                        return
                    else:
                        dots.append(p1)
                elif p2 == p3:
                    if sgn(diff1.y) != sgn(diff2.y):
                        return
                    else:
                        dots.append(p2)
                elif p2 == p4:
                    if sgn(diff1.y) == sgn(diff2.y):
                        return
                    else:
                        dots.append(p2)
                else:
                    return
            else:
                x = p1.x
                a = diff2.y / diff2.x
                b = p3.y - a * p3.x
                y = a * x + b
                dots.append(Point(x, y))
        else:
            if diff2.x == 0:
                x = p3.x
                a = diff1.y / diff1.x
                b = p1.y - a * p1.x
                y = a * x + b
                dots.append(Point(x, y))
            else:
                a1 = diff1.y / diff1.x
                b1 = p1.y - a1 * p1.x
                a2 = diff2.y / diff2.x
                b2 = p3.y - a2 * p3.x
                if a1 == a2:
                    if p1 == p3:
                        if sgn(diff1.x) == sgn(diff2.x):
                            return
                        else:
                            dots.append(p1)
                    if p1 == p4:
                        if sgn(diff1.x) != sgn(diff2.x):
                            return
                        else:
                            dots.append(p1)
                    if p2 == p3:
                        if sgn(diff1.x) != sgn(diff2.x):
                            return
                        else:
                            dots.append(p2)
                    if p2 == p4:
                        if sgn(diff1.x) == sgn(diff2.x):
                            return
                        else:
                            dots.append(p2)
                    else:
                        return
                else:
                    x = (b2-b1) / (a1-a2)
                    y = a1 * x + b1
                    dots.append(Point(x, y))
    else:
        return

def convex_hull(points):
    p0 = min(points)
    points.sort(key=lambda p: (p / p0, (p - p0) ** 1))
    stack = []
    for point in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], point) < 0:
            stack.pop()
        stack.append(point)
    return stack

dots1 = []
dots2 = []
n, m = map(int, input().split())
for i in range(n):
    dots1.append(Point(*map(int, input().split())))
for i in range(m):
    dots2.append(Point(*map(int, input().split())))

dots = []

for i in range(n):
    p1 = dots1[i]; p2 = dots1[(i+1)%n]
    for j in range(m):
        p3 = dots2[j]; p4 = dots2[(j+1)%m]
        add_dot(p1, p2, p3, p4)

for i in dots1:
    flag = True
    for j in range(m):
        if ccw(i, dots2[j], dots2[(j+1)%m]) <= 0:
            flag = False
            break
    if flag:
        dots.append(i)

for i in dots2:
    flag = True
    for j in range(n):
        if ccw(i, dots1[j], dots1[(j+1)%n]) <= 0:
            flag = False
            break
    if flag:
        dots.append(i)

if len(dots) == 0:
    print(0.0)
    sys.exit()

ch = convex_hull(dots)

lg = len(ch)
area = 0
for i in range(lg):
    area += ch[i] @ ch[(i+1)%lg]
print(abs(area/2))