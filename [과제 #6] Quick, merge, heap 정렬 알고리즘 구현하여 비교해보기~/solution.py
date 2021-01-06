import random, timeit
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(50000)

global Qc, Qs, Mc, Ms, Hs, Hc
Qc, Qs, Mc, Ms, Hs, Hc = 0, 0, 0, 0, 0, 0


def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last:
        return
    left, right = first + 1, last
    Qs += 2
    pivot = A[first]
    while left <= right:
        Qc += 1
        while left <= last and A[left] < pivot:
            Qc += 1
            left += 1
        while right > first and A[right] >= pivot:
            Qc += 1
            right -= 1
        if left <= right:  # swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    # place pivot at the right place
    A[first], A[right] = A[right], A[first]  # Pivot을 가운데(작은것과 큰것으로 나누어진 중앙)으로 넣기
    Qs += 1
    quick_sort(A, first, right - 1)  # 작은놈들(S)의 Quick Sort
    quick_sort(A, right + 1, last)  # 큰놈들 (L)의 Quick Sort


def insertion_sort(A, n):
    for i in range(1, n):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j = j - 1
    return A





# Merge 정렬
def merge_sort(A, first, last):  # merge sort A[first] ~ A[last]
    global Ms, Mc
    if first >= last:
        return
    middle = (first + last) // 2
    merge_sort(A, first, middle)
    merge_sort(A, middle + 1, last)

    B = []
    i = first
    j = middle + 1
    while i <= middle and j <= last:
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for i in range(i, middle + 1):
        B.append(A[i])
    for j in range(j, last + 1):
        B.append(A[j])
    for k in range(first, last + 1):
        A[k] = B[k - first]
    Ms += 2 * (last - first + 1)


#Heap 정렬
def heapify_down(A, k, n):
    comp, swap = 0, 0
    while 2 * k + 1 < n:
        L, R = 2 * k + 1, 2 * k + 2
        comp += 2
        if A[L] > A[k]:
            m = L
        else:
            m = k
        if R < n and A[R] > A[m]:
            m = R
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
            swap += 1
        else:
            break
    return comp, swap

def heap_sort(A):
    global Hc, Hs
    # make heap
    n = len(A)
    for i in range(n // 2, -1, -1):
        c, s = heapify_down(A, i, n)
        Hc += c
        Hs += s
    # sort
    for i in range(n - 1, 0, -1):
        Hs += 1
        A[0], A[i] = A[i], A[0]
        n = n - 1
        c, s = heapify_down(A, 0, n)
        Hc += c
        Hs += s



def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            return False
    return True



# 상수 K 이하가 될 때까지만 분할 하는 Quick Sort 구현
def QSort_K(A, first, last, K):
    if first >= last:
        return
    if last - first <= K:
        A[first:last+1] = insertion_sort(A[first:last+1], len(A[first:last+1]))
    else:
        left, right = first + 1, last
        pivot = A[first]
        while left <= right:
            while left <= last and A[left] < pivot:
                left += 1
            while right > first and A[right] >= pivot:
                right -= 1
            if left <= right:  # swap A[left] and A[right]
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        # place pivot at the right place
        A[first], A[right] = A[right], A[first]  # Pivot을 가운데(작은것과 큰것으로 나누어진 중앙)으로 넣기
        QSort_K(A, first, right - 1, K)  # 작은놈들(S)의 Quick Sort
        QSort_K(A, right + 1, last, K)  # 큰놈들 (L)의 Quick Sort

# Merge sort with K
def Msort_K(A, first, last, K):  # merge sort A[first] ~ A[last]
    if first >= last:
        return
    if last - first <= K:
      A[first:last+1] = insertion_sort(A[first:last+1], len(A[first:last+1]))
    else:
      middle = (first + last) // 2
      Msort_K(A, first, middle, K)
      Msort_K(A, middle + 1, last, K)

      B = []
      i = first
      j = middle + 1
      while i <= middle and j <= last:
          if A[i] <= A[j]:
              B.append(A[i])
              i += 1
          else:
              B.append(A[j])
              j += 1

      for i in range(i, middle + 1): B.append(A[i])
      for j in range(j, last + 1): B.append(A[j])
      for k in range(first, last + 1): A[k] = B[k - first]



# n = int(input())
n_times = [100, 500, 1000, 10000, 50000, 100000, 500000]
n = 100
random.seed()
A = [random.randint(-1000, 1000) for i in range(n)]
B = A[:]
C = A[:]

Qc, Qs, Mc, Ms, Hs, Hc = 0, 0, 0, 0, 0, 0

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))
# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert check_sorted(A)
assert check_sorted(B)
assert check_sorted(C)


Qcs, Qss, Mcs, Mss, Hcs, Hss = [], [], [] ,[] ,[] ,[]
q_times, m_times, h_times = [], [], []
for n in n_times:
  random.seed()
  Qc, Qs, Mc, Ms, Hs, Hc = 0, 0, 0, 0, 0, 0
  A = [random.randint(-1000, 1000) for i in range(n)]
  B = A[:]
  C = A[:]

  print("")
  print("Quick sort:")
  q_times.append(timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
  print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
  Qcs.append(Qc)
  Qss.append((Qs))
  
  print("Merge sort:")
  m_times.append(timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
  print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
  Mcs.append(Mc)
  Mss.append(Ms)

  print("Heap sort:")
  h_times.append(timeit.timeit("heap_sort(C)", globals=globals(), number=1))
  print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))
  Hcs.append(Hc)
  Hss.append(Hs)


# time 비교
plt.plot(n_times, q_times, label ='Q_times')
plt.plot(n_times, m_times, label ='M_times')
plt.plot(n_times, h_times, label ='H_times')
plt.legend()
plt.xlabel("n_times")
plt.ylabel("time")
plt.title("Quick, Merge, Heap time")
plt.show()


# Comparsion 비교
plt.plot(n_times, Qcs, label ='Qc')
plt.plot(n_times, Mcs, label ='Mc')
plt.plot(n_times, Hcs, label ='Hc')
plt.legend()
plt.xlabel("n_times")
plt.ylabel("comparsion")
plt.title("Quick, Merge, Heap Comparsion times")
plt.show()


# Swap 비교
plt.plot(n_times, Qss, label ='Qs')
plt.plot(n_times, Mss, label ='Ms')
plt.plot(n_times, Hss, label ='Hs')
plt.legend()
plt.xlabel("n_times")
plt.ylabel("swap")
plt.title("Quick, Merge, Heap swap times")
plt.show()



# 상수 K개 이하시 Insertion sort를 사용한 quick sort의 최적 K 찾기
Qsort_times = []
for k in range(40,9,-1):
  random.seed()
  A = [random.randint(-1000, 1000) for i in range(n)]
  Qsort_times.append(timeit.timeit("QSort_K(A, 0, n-1, k)", globals=globals(), number=1) )


plt.plot(list(range(40,9,-1)), Qsort_times)
plt.xlabel("K")
plt.ylabel("times")
plt.title("Quick + Insertion Sorting with K")
plt.show()


# Quick sort 와 Quick + Insertion Sort 비교 K=20
Qsort_K_times = []
Qsort_times = []
n_times = [100, 500, 1000, 10000, 50000, 100000, 500000]
for n in n_times:
  random.seed()
  print(n)
  A = [random.randint(-1000, 1000) for i in range(n)]
  B = A[:]
  Qsort_K_times.append(timeit.timeit("QSort_K(A, 0, n-1, 20)", globals=globals(), number=1) )
  Qsort_times.append(timeit.timeit("quick_sort(B, 0, n-1)", globals=globals(), number=1) )

plt.plot(n_times, Qsort_K_times, label='Quick+Insertion')
plt.plot(n_times, Qsort_times, label='Quick')
plt.legend()
plt.xlabel("n_times")
plt.ylabel("time")
plt.title("Quick + Insertion vs Quick")
plt.show()



# 상수 K개 이하시 Insertion sort를 사용한 Merge sort의 최적 K 찾기
Msort_times = []
n = 5000
for k in range(40,9,-1):
  random.seed()
  A = [random.randint(-1000, 1000) for i in range(n)]
  Msort_times.append(timeit.timeit("Msort_K(A, 0, n-1, k)", globals=globals(), number=1) )

plt.plot(list(range(40,9,-1)), Msort_times)
plt.xlabel("K")
plt.ylabel("times")
plt.title("Merge + Insertion Sorting with K")
plt.show()

# Merge sort 와 Quick + Insertion Sort 비교 K=25
Msort_K_times = []
Msort_times = []
n_times = [100, 500, 1000, 10000, 50000, 100000, 500000]
for n in n_times:
  random.seed()
  print(n)
  A = [random.randint(-1000, 1000) for i in range(n)]
  B = A[:]
  Msort_K_times.append(timeit.timeit("Msort_K(A, 0, n-1, 25)", globals=globals(), number=1) )
  Msort_times.append(timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1) )

plt.plot(n_times, Msort_K_times, label='Merge+Insertion')
plt.plot(n_times, Msort_times, label='Merge')
plt.legend()
plt.xlabel("n_times")
plt.ylabel("time")
plt.title("Merge + Insertion vs Merge")
plt.show()