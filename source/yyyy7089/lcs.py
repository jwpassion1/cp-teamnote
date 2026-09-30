s1 = input()
s2 = input()

l = [[0]*(len(s2)+1) for i in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            l[i][j] = l[i-1][j-1] + 1
        else:
            l[i][j] = max(l[i-1][j], l[i][j-1])
# end here and print l[-1][-1] if only need length

i = len(s1)
j = len(s2)
lcs = ''
while True:
    if i==0:
        break
    if j==0:
        break
    if l[i-1][j] == l[i][j]:
        i -= 1
        continue
    if l[i][j-1] == l[i][j]:
        j -= 1
        continue
    lcs += s1[i-1]
    i -= 1
    j -= 1
lcs = lcs[::-1]

print(l[-1][-1])
print(lcs)