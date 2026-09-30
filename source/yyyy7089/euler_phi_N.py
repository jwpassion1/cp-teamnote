max_N = 10_000
sieve = list(range(max_N+1))
for i in range(2, max_N+1):
    if i == sieve[i]:
        for j in range(i, max_N+1, i):
            sieve[j] = sieve[j] // i * (i-1)

pfs = []
x = 0
for i in sieve:
    x += i
    pfs.append(x)
for i in range(int(input())):
    i, j = map(int, input().split())
    print(i, pfs[j]+1)