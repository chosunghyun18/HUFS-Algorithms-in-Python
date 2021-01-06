#%%
import numpy as np

def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])
#%%
flag =True
def subset_sum(k):
    global flag
    v_sum = np.matmul(x, A)
    if k == len(A):
        if v_sum == S:
            print_subset(x)
            flag=False
        if np.sum(x) == 0 and flag:
            print([])
        return
    else:
        # x[k] =1 경우
        if v_sum + A[k] <=S:
            x[k] = 1
            if v_sum + A[k] == S or subset_sum(k+1):
                subset_sum(k+1)
        # x[k] = 0인 경우
        x[k]=0
        if subset_sum(k+1):
            subset_sum(k+1)


# 아래 코드는 수정하지 말고 그대로 사용할 것
# A = list(set(int(x) for x in input().split()))

#%%
A = list(set(int(x) for x in '8 7 6 5 3 10 9'.split()))
A.sort()
# S = int(input())
S = int('15')
x = [0]*len(A)
subset_sum(0)

# %%
# %%
