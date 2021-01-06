def reconstruct(S, L):
	permuts= list(range(len(S)))
	max_num = max(permuts)
	A = [0,1,2,3,4]
	for i in range(len(S)//2):
		if S[max_num-i] == max_num:
			A[i] = permuts.pop()
		else:
			A[i] = permuts[S[i]:][0]
			rest = permuts[S[i]:]
			del rest[0]
			permuts = permuts[:S[i]] + rest




# def reconstruct(S, L):
# 	permut= list(range(len(S)))
# 	A = []
# 	max_int = max(permut)
# 	for i in range(len(S)):
# 		if L[i] == max_int:
# 			A.append(permut.pop(0))
# 		else:
# 			A.append(permut.pop(-(L[i]+1)))
# 	return A


'''
max_int = max(permut) -> O(n)
A.append(permut.pop(0)) -> O(n) + 1
A.append(permut.pop(-(L[i]+1))) -> O(n) + 1

T(n) = n * (2n + c) +  c
T(n) = 2n^2+c
T(n) = O(N^2)


'''


# S와 L을 차례로 읽어들임
# S = [int(x) for x in '0 1 0 1 0'.split()]
# L = [int(x) for x in '1 0 1 0 0'.split()]
S = [int(x) for x in '0 1 1 3 3'.split()]
L = [int(x) for x in '4 2 2 0 0'.split()]
A = reconstruct(S, L)

print(A)
# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# import time
# start = time.process_time()
# reconstruct(S, L)
# stop = time.process_time()
# print("수행시간 %0.10f초" %(stop-start))
# -> 수행시간 0.0000570000초

# 2. 수행시간 T(n)을 Big-O료 표기해보자
