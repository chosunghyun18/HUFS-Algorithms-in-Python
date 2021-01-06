'''
    Code by Chan-Su Shin (신찬수, 한국외대, 컴전학부)
    알고리즘 수업용 코드
    sort_analysis.csv를 읽어 실시간 그래프를 그려주는 코드
    2020-05-07
'''

import matplotlib.pyplot as plt
import pandas as pd
import random
from matplotlib.animation import FuncAnimation
import math

plt.style.use('seaborn')
csv_filename = "sort_analysis.csv"

def animate_csv(i):
    data = pd.read_csv(csv_filename)
    n = data['n']
    Qc = data['comps_QS']
    Qs = data['swaps_QS']
    Mc = data['comps_MS']
    Ms = data['swaps_MS']
    Hc = data['comps_HS']
    Hs = data['swaps_HS']

    Q = [a+b for a, b in zip(Qc, Qs)]
    M = [a+b for a, b in zip(Mc, Ms)]
    H = [a+b for a, b in zip(Hc, Hs)]
    L = [int(3*k*math.log2(k)) for k in n]

    plt.cla()
    plt.plot(n, L, label="3nlogn")
    plt.plot(n, Q, label="Quick sort")
    plt.plot(n, M, label="Merge sort")
    plt.plot(n, H, label="Heap sort")
    plt.xlabel("n")
    plt.ylabel("number of comparisons + swaps + moves")
    plt.legend(loc="upper left")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate_csv, interval=600)

plt.tight_layout()
plt.show()
