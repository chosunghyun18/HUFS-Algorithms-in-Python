def fractional_knapsack(n, size, profit, K):
	# n개의 아이템, 크기 size[], 가치 profit[], 배낭의 현재 빈 공간 K
	0. if K <= 0: return 0
	1. 가치의 내림차순으로 (size[i], profit[i])를 정렬되어 있다고 가정(아니면, 정렬함)
	2. s = 현재까지 선택한 아이템의 크기 합 = 0 (초기 값)
	   p = 현재까지 선택한 아이템의 가치 합 = 0 (초기 값)
	3. for i in range(n):
			if s + size[i] <= K: # 배낭에 쏙 들어가면 전체 선택
				p += profit[i]
				s += size[i]
			else: # 넘치면 잘라서 선택
				p += (K-s) * (p[i]/s[i])
				s = K
				break
	5. return p
