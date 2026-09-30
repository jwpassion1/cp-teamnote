def phi(N):
    v = 1
    f = sorted(factorize(N))
    for i in f:
        d = 0
        while N % i == 0:
            d += 1
            N //= i
        if d > 0:
            v *= pow(i, d-1) * (i-1)
    if N > 1:
        v *= N - 1
    return v