#%%
def reverse(L, a):
    n = len(L)
    if a< n//2:
        L[a], L[n-1-a] =  L[n-1-a] ,L[a]
        reverse(L, a+1)
L = list('This is a pen!')

reverse(L, 0)
print("".join(L))


# %%

def f2(n):
    j =1
    c = 0
    while j<=n:
        j*=2
        c+=1

    return c
for i in range(1, 17):
    print(i, f2(i))
# %%
