import numpy as np
import math

"""
12
ape eats apple cider a lot.
"""

W = int("5")
words = "ab c dc".split()
# code below

P = [[0] * len(words) for _ in words]
for i, word in enumerate(words):
    P[i][i] = (W - len(word)) ** 3


for j in range(1, len(words)):
    for i in range(j - 1, -1, -1):
        P[i][j] = math.inf
        for k in range(i, j + 1):
            if k < j:
                penalty = P[i][k] + P[k + 1][j]
            else:
                right = W - len("".join(words[i : j + 1])) - (j - i)
                if right >= 0:
                    penalty = right ** 3
            if penalty <= P[i][j]:
                P[i][j] = penalty


print(np.array(P))
