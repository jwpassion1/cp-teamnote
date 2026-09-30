P = 2_147_483_647

def add_mat(a, b):
    for i in range(N):
        mat[a][i] = (mat[a][i] + mat[b][i]) % P
def mul_mat(a, b):
    for i in range(N):
        mat[a][i] = (mat[a][i] * b) % P
def sub_mat(a, b):
    for i in range(N):
        mat[a][i] = (mat[a][i] - mat[b][i]) % P
def count_nonzero_mat():
    cnt = 0
    for i in range(N):
        if sum(mat[i]) != 0:
            cnt += 1
    return cnt

N, M = map(int, input().split())
mat = [[0] * N for i in range(N)]

for i in range(M):
    a, b = sorted(list(map(int, input().split()))); a -= 1; b -= 1
    x = random.randrange(1, P)
    mat[a][b] = x; mat[b][a] = (-x)%P

for x in range(N):
    for y in range(N-1):
        if mat[y][x] == 0:
            continue
        if mat[y+1][x] == 0:
            add_mat(y+1, y)
        v1 = mat[y][x]; v2 = mat[y+1][x]
        mul_mat(y, v2); mul_mat(y+1, v1)
        sub_mat(y, y+1)

if count_nonzero_mat() == N:
    print(1)
else:
    print(0)