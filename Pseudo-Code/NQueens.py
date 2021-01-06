
#%%
sol = 0
n = 4
x = [0] * (n+1)
#%%
def B(k, col):
    for row in range(1,k):
        if x[row] == col or abs(k-row)== abs(col- x[row]):
            return False
    else: return True

#%%
def solution(k):
    global sol
    if k>n:
        sol+=1
        return print(x[1:])
    for col in range(1,n+1):
        if B(k, col):
            x[k] = col
            solution(k+1)

solution(1)
print(sol)


# %%

# %%
