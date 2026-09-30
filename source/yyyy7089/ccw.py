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


def ccw(p1: Point, p2: Point, p3: Point):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def convex_hull(points):
    p0 = min(points)
    points.sort(key=lambda p: (p / p0, (p - p0) ** 1))
    stack = []
    for point in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack

n = int(input())
l = []
for i in range(n):
    l.append(Point(*map(int, input().split())))

ch = convex_hull(l)
