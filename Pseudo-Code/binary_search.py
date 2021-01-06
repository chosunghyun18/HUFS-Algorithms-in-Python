#%%
array = [0,2,4,6,8,10,12,14,16,18]
#%%
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
# %%
def binary_search(array, target, start, end):
    while start<= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid +1
    return None
# %%
binary_search(array, 6, 0, len(array)-1)
# %%
array[3]
# %%
