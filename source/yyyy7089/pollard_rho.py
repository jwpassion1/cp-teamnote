def factorize(N):
    if N == 1:
        return []
    if N % 2 == 0:
        l = []
        while N % 2 == 0:
            l.append(2)
            N //= 2
        if N == 1:
            return l
        else:
            return l + factorize(N)
    if is_prime(N):
        return [N]
    while True:
        C = random.randrange(1, N)
        x = random.randrange(1, N)
        l = [x]
        sz = 0
        while True:
            x = (x * x + C) % N
            l.append(x)
            if sz % 2 == 0 and sz > 0:
                g = math.gcd(l[sz]-l[sz//2], N)
                if g != 1:
                    if g == N:
                        break
                    else:
                        return factorize(g) + factorize(N // g)
            sz += 1