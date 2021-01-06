
# A = [5, 9, 10, 2 ,4, 5, 12, 8, -6, 1]
A = "5 9 10 2 4 5 12 8 -6 -2 1"
A = [int(i) for i in A.split()]


def min_max2(A):
    if type(A) == int or len(A)==1:
        return A[0], A[0]
    if len(A) == 2:
        left, right = A
        if type(left) == int:
            if left < right:
                m = left
                M = right
                return m, M
            else:
                m = right
                M = left
                return m, M

    mid = len(A)//2
    A = min_max2(A[:mid]) , min_max2(A[mid:])
    left, right =A
    if len(left)==2 and len(right)==2:
        m = left[0] if left[0] < right[0] else right[0]
        M = left[1] if left[1] > right[1] else right[1]
        return m, M
    return A

m, M = min_max2(A)
print(m, M)

