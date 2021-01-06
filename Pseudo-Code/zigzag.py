#%%
def zigzag(arr, n):
	'''Z[i][0] = Length of the longest Zig-Zag subsequence
		ending at index i and last element is greater
		than its previous element
	Z[i][1] = Length of the longest Zig-Zag subsequence
		ending at index i and last element is smaller
		than its previous element '''

	# Z = [[1 for i in range(2)] for i in range(n)]
	low = [1 for i in range(n)]
	high = [1 for i in range(n)]


	res = 1 # Initialize result

	# Compute values in bottom up manner '''
	for i in range(1, n):

		# Consider all elements as previous of arr[i]
		for j in range(i):

			# If arr[i] is smaller, then check with Z[j][0]
			if( arr[j] > arr[i] and low[i] < high[j] + 1): #LOW
				low[i] = high[j] + 1
			# If arr[i] is greater, then check with Z[j][1]
			if (arr[j] < arr[i] and high[i] < low[j] + 1): #HIGH
				high[i] = low[j] + 1


		# Pick maximum of both values at index i '''
		if (res < max(high[i], low[i])):
			res = max(high[i], low[i])

	return res

arr = [10, 22, 9, 33, 49, 50, 31, 60]
n = len(arr)
print("Length of Longest Zig-Zag subsequence is",
									zigzag(arr, n))

# This code is contributed by Mohit Kumar

#%%
A =[ 3,-1, 2, 5, 7, 4, 5, 9,8 ]
zigzag(A)
# %%
