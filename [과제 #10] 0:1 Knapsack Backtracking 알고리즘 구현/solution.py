# %%
import numpy as np
#%%
def fractional_knapsack(n ,size, profit, K):
    # n개의 아이템, size=크기, profit = 가치, K = 현재 배낭의 빈 공간
    if K <= 0: return 0
    # 가치의 내림차순으로 (size[i], profit[i])를 정렬함(가정)
    #s = 현재까지 선택한 item의 합, 초기값=0
    s = 0
    #p = 현재까지 선택한 item의 가치 합, 초기값=0
    p = 0

    for i in range(n):
        if s + size[i]<=K: #배낭에 들어 갈 수 있으면 전체 선택
            p+= profit[i]
            s+= size[i]
        else: # 넘치면 잘라서 선택
            p += (K-s) * (profit[i]/size[i])
            s = K
            break
    return p
# %%
def Knapsack(i, T): #x[i] =1, x[i] =0 인경우를 각각 시도
    # T는 배낭의 남은 공간을 의미
    global MaxProfit, solution
    if i>=n or T<=0:
        return

    s = sum([a*b for a,b in zip(x,size)])
    p = sum([a*b for a,b in zip(x,profit)])

    # item(i)를 선택하여 배낭에 넣는 경우 = x[i]=1 이라면
    # i+1 이후 하이템에 대해, 남은 배낭공간(T-size[i])에 fractional로 채울 수 있는 최대 가치 계산

    x[i] =1
    B = fractional_knapsack(n - (i+1), size[i+1:], profit[i+1:], T - size[i])
    if s+size[i] <= K and  (p + profit[i] +B) >MaxProfit:
        if p+ profit[i] > MaxProfit:
            MaxProfit = p + profit[i]
            solution = x
        Knapsack(i+1, T-size[i])


    x[i]= 0
    B = fractional_knapsack(n - (i+1), size[i+1:], profit[i+1:], T)
    if (p + B) >=MaxProfit:
        Knapsack(i+1, T)






# %%
K = 16
n = 4
size = list(map(int, "2 5 10 5".split()))
profit = list(map(int, "40 30 50 10".split()))
SP = sorted(zip(size, profit), key=lambda x: x[1]/x[0], reverse=True)
size, profit = [s for s, p in SP], [p for s,p in SP]
x = [0]*n
MaxProfit = 0 # 현재까지 가장 가치가 큰 값
solution = []
S = []
Knapsack(0,K)
print(MaxProfit)


# %%

# %%
