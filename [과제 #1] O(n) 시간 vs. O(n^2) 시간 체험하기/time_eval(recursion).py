# -*- coding:utf-8 -*-
import time, random, sys
sys.setrecursionlimit(10000)

def evaluate_n2(A, x, *args):
    fx = 0
    tmp = x
    for i, a in enumerate(A):
        if i == 0:
            x =1
        for _ in range(i - 1):
            x *= tmp
        fx += a * x
        x = tmp
    return fx


def evaluate_n(A, x, n):
    if n == 1:
        return A[-1]
    return A[-n] + x * evaluate_n(A, x, n - 1)


random.seed()  # random 함수 초기화
n = 5000
A = [random.randint(-999, 999) for _ in range(n)]
x = random.randint(-99, 99)


# evaluate_n(A,x, len(A))
# evaluate_n2(A,x)


def time_measure(eval_func, A, x, n=None):
    before = time.process_time()
    eval_func(A, x, n)
    after = time.process_time()
    return print(after - before)


time_measure(evaluate_n, A, x, len(A))
time_measure(evaluate_n2, A, x)
