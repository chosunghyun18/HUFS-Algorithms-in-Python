#%%
def selection_sort(A, n):
    for i in range(n-1, 0, -1):
        max_index = i
        for j in range(i+1):
            if A[max_index] < A[j]:
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
A = [9,8,7,0,3,1,6,2,4,8]
selection_sort(A, len(A))
# %%
