# Ignition
# T[k] = S[k-1] + S[k-2] + 2 * (L[k-3]+S[k-3])

n = 3

S = [0] * (n +1)
L = [0] * (n +1)

L[0], L[1] = 0, 0
S[0], S[1] = 1, 1


for k in range(2, n+1):
    if k == 2:
        L[k] = L[k-1] + 0
        S[k] = S[k-1] + S[k-1] + 2*L[k]
        continue

    L[k] = L[k-1] + S[k-3]
    S[k] = S[k-1] + S[k-2] + 2*L[k]

print(S[-1])
