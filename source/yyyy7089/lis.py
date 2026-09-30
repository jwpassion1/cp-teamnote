n = int(input())
l = list(map(int,input().split()))

nl = [l[0]]
lengl = [1]
length = 1

for i in range(1, n):
    x = l[i]
    
    if x > nl[-1]:
        nl.append(x)
        length += 1
        lengl.append(length)
    elif x <= nl[0]:
        nl[0] = x
        lengl.append(1)
    else:
        Llimit = 0
        Rlimit = length
        while True:
            index = (Llimit+Rlimit)//2
            if x > nl[index]:
                Llimit = index
            else:
                Rlimit = index
            if Llimit == Rlimit - 1:
                break
        nl[Rlimit] = x
        lengl.append(Rlimit+1)

print(length)

fl = []
for i in range(n-1, -1, -1):
    if lengl[i] == length:
        if len(fl) == 0 or l[i] != fl[-1]:
            length -= 1
            fl.append(l[i])
for i in fl[::-1]:
    print(i,end=' ')