#%%
array = [5,7,9,0,3,1,6,2,4,8]

# %%
def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    S, M, L = [],[],[]

    for x in A:
        if x > pivot:
            L.append(x)
        elif x < pivot:
            S.append(x)
        else:
            M.append(x)
    return quick_sort(S) + M + quick_sort(L)
# %%
quick_sort(array)
