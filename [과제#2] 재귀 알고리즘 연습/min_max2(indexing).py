# -*- coding:utf-8 -*-

def min_max2(A, left, right):
    if right - left == 1:
        if A[left] < A[right]:
            return A[left], A[right]
        else:
            return A[right], A[left]

    if left == right:
        return A[left], A[left]
    mid = (left + right) // 2
    first, second = min_max2(A, left, mid), min_max2(A, mid + 1, right)
    m = first[0] if first[0] < second[0] else second[0]
    M = first[1] if first[1] > second[1] else second[1]
    return m, M


A = "5 4 1 0 8 3 1"
A = A.split()
A = [int(i) for i in A]
# n개의 정수를 읽어 A에 저장
m, M = min_max2(A, 0, len(A) - 1)
print(m, M)
