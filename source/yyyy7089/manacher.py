s = input().strip()
S = '#'+'#'.join(s)+'#'

lg = len(S)

a = []
M = -1
R = -1
mlg = 1
for i in range(lg):
    if i > R:
        a.append(0)
    else:
        a.append(min(a[M*2-i], R - i))
    while True:
        if i-a[i] < 0 or i+a[i] >= lg:
            break
        if S[i-a[i]] == S[i+a[i]]:
            a[i] += 1
            continue
        break
    if i + a[i] - 1 > R:
        R = i + a[i] - 1
        M = i
    mlg = max(mlg, a[i]-1)
print(mlg)