

#%%
global Qc, Qs, Mc, Ms, Hs, Hc
Qc, Qs, Mc, Ms, Hs, Hc = 0, 0, 0, 0, 0, 0

# Merge 정렬
def merge_sort(A, first, last):  # merge sort A[first] ~ A[last]
    global Ms, Mc
    if first >= last:
        return
    mid = (first + last) // 2
    merge_sort(A, first, mid)
    merge_sort(A, mid + 1, last)

    B = []
    i = first
    j = mid + 1
    while i <= mid and j <= last:
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for i in range(i, mid + 1):
        B.append(A[i])
    for j in range(j, last + 1):
        B.append(A[j])
    for k in range(first, last + 1):
        A[k] = B[k - first]
    Ms += 2 * (last - first + 1)


# %%

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr)-1)
# %%
