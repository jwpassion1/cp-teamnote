scc = scc[::-1]

is_okay = True
for i in scc:
    for j in i:
        if j^1 in i:
            is_okay = False
            break
    if not is_okay:
        break
if is_okay:
    print(1)
else:
    print(0)

if is_okay:
    values = [-1] * n
    for i in scc:
        okay_to_zero = True
        for j in i:
            if values[j] == 1:
                okay_to_zero = False
                break
        if okay_to_zero:
            for j in i:
                values[j] = 0
                values[j^1] = 1
        else:
            for j in i:
                values[j] = 1
                values[j^1] = 0
    for i in values[::2]:
        print(i, end=' ')