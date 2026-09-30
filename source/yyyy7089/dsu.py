class union:
    def __init__(self, size = 10**6):
        self.l = [i for i in range(size)]
        
    def find(self, i):
        if self.l[i] == i:
            return i
        self.l[i] = self.find(self.l[i])
        return self.l[i]
    
    def union(self, i, j):
        self.l[self.find(j)] = self.find(i)
        return