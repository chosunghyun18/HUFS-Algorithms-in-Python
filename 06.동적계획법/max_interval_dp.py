def max_interval(A):
    S = [0] * len(A)
    S[0] = A[0]

    for k in range(1,len(A)):
        S[k] = max(S[k-1]+A[k], A[k])

    return max(S)

A = [1, -1, 3, -4, 5, -4, 6,2]
