def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x == 1 or x & 1 == 0:
        return False
    if x < 1_373_653:
        prime_test = [2, 3]
    else:
        prime_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    w, r = x - 1, 0
    while w & 1 == 0:
        w >>= 1
        r += 1
    for p in prime_test:
        v = pow(p, w, x)
        if v == 1 or v == x - 1:
            continue
        for _ in range(r - 1):
            v = pow(v, 2, x)
            if v == 1:
                return False
            if v == x - 1:
                break
        else:
            return False
    return True