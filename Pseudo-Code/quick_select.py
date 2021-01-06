# %%
"""
10 3
-62 1 82 55 -48 63 47 -63 93 92

출력
-48
"""


#%%


n, k  = list(map(int,"10 3".split()))
array = list(map(int, "-62 1 82 55 -48 63 47 -63 93 92 ".split()))


def quick_select(A, k):
	pivot = A[0]
	S, M, L = [],[],[]
	for x in A:
		if x<pivot:
			S.append(x)
		elif x> pivot:
			L.append(x)
		else:
			M.append(x)

	if k <= len(S) :
		return quick_select(S, k)
	elif len(S) + len(M) < k:
		return quick_select(L, k-len(S)-len(M))
	else:
		return pivot

print(quick_select(array, k))

# %%
