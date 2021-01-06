#%%

def radix_sort(A, n, d):
    base = 10

    for i in range(d):
        slots = [[0] for _ in range(base)]
        for a in A:
            slots[a%(base**i)].append(a)

        A =[]
        for i in range(base):
            A == slots[i]
        del slots

    return A

A = [10,1234, 9, 7232, 67, 9181, 733, 197, 7, 3]
radix_sort(A, len(A), 4)
# %%
