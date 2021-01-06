import math
import numpy as np

"""
6
2 5 3 5 10 2 4
"""

n = int('3') # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in '10 100 5 50'.split()] # M_i = p_i x p_{i+1}
C = [[0]*n for _ in range(n)] # 비용을 저장할 2차원 리스트 C 초기화



for j in range(1, n):
    for i in range(j-1, -1, -1) :
        C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
        for k in range(i, j):
            print(i, j ,k)
            cost = C[i][k] + C[k+1][j] + P[i-1]*P[k]*P[j]
            if cost<=C[i][j]:
                C[i][j] = cost

print(np.array(C))
