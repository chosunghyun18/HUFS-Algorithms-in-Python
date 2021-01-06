'''
    Code by Chan-Su Shin (신찬수, 한국외대, 컴전학부)
    알고리즘 수업용 코드
    - quick, merge, heap 정렬에서 비교, 이동(교환) 횟수 실험
    - n = 100개부터 10,000개까지 100개씩 증가하면서 랜덤 정수 생성해 실험
    - 실험 수치를 sort_analysis.csv에 저장
    2020-05-07
'''
import random, timeit, csv, time

def quick_sort(A, first, last):
    global Qs, Qc
    # return comparison number and swap number
    if first >= last: return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
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
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)

def merge_sort(A, first, last):
    global Mc, Ms
    # return comparison number and swap number
    if first >= last: return
    middle = (first+last)//2
    merge_sort(A, first, middle)
    merge_sort(A, middle+1, last)

    B = []
    i = first
    j = middle+1
    while i <= middle and j <= last:
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for i in range(i, middle+1):
        B.append(A[i])
    for j in range(j, last+1):
        B.append(A[j])
    for k in range(first, last+1):
        A[k] = B[k-first]
    Ms += 2*(last-first+1)

def heap_sort(A):
    global Hc, Hs
    # make heap
    n = len(A)
    for i in range(n//2, -1, -1):
        c, s = heapify_down(A, i, n)
        Hc += c
        Hs += s
    # sort
    for i in range(n-1, 0, -1):
        Hs += 1
        A[0], A[i] = A[i], A[0]
        n = n - 1
        c, s = heapify_down(A, 0, n)
        Hc += c
        Hs += s

def heapify_down(A, k, n):
    comp, swap = 0, 0
    while 2*k+1 < n:
        L, R = 2*k + 1, 2*k + 2
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

def check_sorted(A):
	sorted = True
	for i in range(n-1):
		if A[i] > A[i+1]:
		    return False
	return True


fieldnames = ['n', 'comps_QS', 'swaps_QS', 'comps_MS', 'swaps_MS', 'comps_HS', 'swaps_HS']
with open('sort_analysis.csv', 'w') as f_csv:
    csv_writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
    csv_writer.writeheader()

for n in range(100, 100000, 100):
    Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

    random.seed()
    A = []
    for i in range(n):
        A.append(random.randint(-1000, 1000))
    B = A[:]
    C = A[:]

    print("n =", n)
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
    assert(check_sorted(A))
    assert(check_sorted(B))
    assert(check_sorted(C))

    with open('sort_analysis.csv', 'a') as f_csv:
        csv_writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        info = {
            'n': n,
            'comps_QS': Qc,
            'swaps_QS': Qs,
            'comps_MS': Mc,
            'swaps_MS': Ms,
            'comps_HS': Hc,
            'swaps_HS': Hs
        }
        csv_writer.writerow(info)

    time.sleep(0.2)
