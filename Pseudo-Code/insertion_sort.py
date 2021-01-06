
#%%
array = [7, 5, 9, 0, 3, 1, 6,2,4,8]
n = len(array)
# %%
for i in range(1,n):
    for j in range(i, 0, -1 ):
        if array[j-1] > array[j]:
            array[j-1] , array[j] = array[j], array[j-1]
        else:
            break
# %%
