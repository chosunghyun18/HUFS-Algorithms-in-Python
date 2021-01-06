def reconstruct(B):
	permut = list(range(len(B)))
	A = []
	max_num = max(permut)
	for i in permut[::-1]:
		if B[i] == max_num:
			A.append(permut.pop())
		else:
			A.append(permut.pop(B[i]))
	A.reverse()
	return A



B = [int(x) for x in '0 0 0 0 0'.split()]
A = reconstruct(B)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
import time
start = time.process_time()
reconstruct(B)
stop = time.process_time()
print("수행시간 %0.10f초" %(stop-start))


# 2. 수행시간 T(n)을 Big-O료 표기해보자
#
'''
max_num = max(permut) -> O(N)

'''
