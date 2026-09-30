def failure(S):
    sl = len(S)
    f = [0] * sl
    i = 1; j = 0 #i = check (current) index; j = length
    while i < sl:
        if S[j] == S[i]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = f[j-1]
        else:
            i += 1
    return f

def kmp(L, S, F):
    fl = len(F)
    sl = len(S)
    if fl > sl:
        return []
    i = 0; j = 0 # i = current index, j = length found
    ll = []
    while i < sl:
        if F[j] == S[i]:
            i += 1
            j += 1
            if j == fl:
                ll.append(i-j)
                j = L[j-1]
        else:
            if j > 0:
                j = L[j-1]
            else:
                i += 1
    return ll

find = input()
s = input()
l = failure(find)
print(kmp(l, s, find))
