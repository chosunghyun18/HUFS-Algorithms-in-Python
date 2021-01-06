def Knapsack(i, T): # x[i] = 1인 경우와 0인 경우를 각각 시도함
	# T는 배낭의 남은 공간을 의미함
	if i >= n or T <= 0:
		print(x)
		return

	s, p = 현재 상태에서 선택된 크기 합, 가치 합

	# 아이템 i를 선택하여 배낭에 넣는 경우: x[i] = 1 이라면?
	# i+1 이후 아이템에 대해, 남은 배낭공간(T-size[i])에 fractional로 채울 수 있는 최대 가치 계산
	x[i] = 1
	if s+size[i] <= K: # 계속 탐색해야 한다면
		B = fractional_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T-size[i])
		if p+profit[i]+B > MaxProfit: # 계속 탐색을 해야 한다면
			MaxProfit 업데이트 + x를 solution으로 카피(기록)
			Knapsack(i+1, T-size[i])

	# 아이템 i를 선택하지 않는 경우: x[i] = 0 이라면?
	x[i] = 0
	B = fractional_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T)
	if (p + B) > MaxProfit: # 계속 탐색해야 한다면
		Knapsack(i+1, T)

1. n, size, profit, K 입력으로 주어짐
2. x = [0, 0, ..., 0] # 아이템 i가 선택되면 x[i] = 1, 아니면 x[i] = 0이 됨
3. MaxProfit = 현재까지 가장 큰 가치 값 [전역변수]
4. solution = [] [전역변수]
4. Knapsack(0, K) # [주의] 아이템의 번호가 0부터 시작한다고 가정!
