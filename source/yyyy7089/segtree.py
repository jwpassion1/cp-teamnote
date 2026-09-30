class segtree:
    def __init__(self, N):
        self.size = 1 << math.ceil(math.log2(N))
        self.tree = [0] * (self.size << 1)

    def set(self, idx, val):
        self.tree[idx | self.size] = val
        return

    def init(self):
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        return

    def query(self, left, right):
        left |= self.size
        right |= self.size
        ret = 0
        while left <= right:
            if left & 1:
                ret += self.tree[left]
                left += 1
            if ~right & 1:
                ret += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return ret

    def update(self, idx, val):
        idx |= self.size
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx >> 1] = self.tree[idx] + self.tree[idx ^ 1]
            idx >>= 1
        return

INF = 1 << 31