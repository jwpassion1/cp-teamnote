class lazyseg:
    def __init__(self, N):
        self.h = math.ceil(math.log2(N))
        self.size = 1 << self.h
        self.segtree = [0 for _ in range(self.size << 1)]
        self.length = [1 for _ in range(self.size << 1)]
        self.lazy = [0 for _ in range(self.size)]

    def assign(self, i, val):
        self.segtree[i | self.size] = val

    def init(self):
        for i in reversed(range(1, self.size)):
            self.segtree[i] = self.segtree[i << 1] + self.segtree[i << 1 | 1]
            self.length[i] = self.length[i << 1] + self.length[i << 1 | 1]

    def propagate(self, i, val):  # node update
        self.segtree[i] += val * self.length[i]
        if i < self.size:
            self.lazy[i] += val

    def push(self, i):
        self.propagate(i << 1, self.lazy[i])
        self.propagate(i << 1 | 1, self.lazy[i])
        self.lazy[i] = 0

    def pull(self, i):  # node + node -> node
        self.segtree[i] = self.segtree[i << 1] + self.segtree[i << 1 | 1]

    def update(self, left, right, val):
        left |= self.size
        right |= self.size
        for i in reversed(range(1, self.h + 1)):
            if not left >> i << i == left:
                self.push(left >> i)
            if not right + 1 >> i << i == right + 1:
                self.push(right >> i)
        l, r = left, right
        while l <= r:
            if l & 1:
                self.propagate(l, val)
                l += 1
            if ~r & 1:
                self.propagate(r, val)
                r -= 1
            l >>= 1
            r >>= 1
        for i in range(1, self.h + 1):
            if not left >> i << i == left:
                self.pull(left >> i)
            if not right + 1 >> i << i == right + 1:
                self.pull(right >> i)

    def query_point(self, i):
        i |= self.size
        for j in reversed(range(1, self.h + 1)):
            self.push(i >> j)
        return self.segtree[i]

    def query(self, left, right):
        l, r = 0, 0
        left |= self.size
        right |= self.size
        for i in reversed(range(1, self.h + 1)):
            if not left >> i << i == left:
                self.push(left >> i)
            if not right + 1 >> i << i == right + 1:
                self.push(right >> i)
        while left <= right:
            if left & 1:
                l += self.segtree[left]
                left += 1
            if ~right & 1:
                r += self.segtree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return l + r