import random
def quickSort(A, first, last):
    if first >= last: return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] >= pivot:
            right -= 1
        if left <= right: # swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    # place pivot at the right place
    A[first], A[right] = A[right], A[first]
    quickSort(A, first, right-1)
    quickSort(A, right+1, last)

n = int(input("n = "))
random.seed()
A = [random.randint(1, 100) for x in range(n)]
print(A)
quickSort(A, 0, len(A)-1)
print(A)
