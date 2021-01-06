import time, random, sys
import matplotlib.pyplot as plt
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
n = 1000
A = [random.randint(-999, 999) for _ in range(n)]
x = random.randint(-99, 99)

# n = 1000


def time_measure(eval_func, A, x, n=None):
    before = time.process_time()
    eval_func(A, x, n)
    after = time.process_time()
    return (after - before)


times = range(1000, 10000, 1000)
n_time = []
n2_time = []
for n in times:
    A = [random.randint(-999, 999) for _ in range(n)]
    x = random.randint(-99, 99)
    n_time.append(time_measure(evaluate_n, A, x, len(A)))
    n2_time.append(time_measure(evaluate_n2, A, x))


# time_measure(evaluate_n,A,x)
# time_measure(evaluate_n2,A,x)


plt.plot(n_time, label="n")
plt.plot(n2_time, label="n^2")
# plt.ylim(top=2)
plt.legend()
plt.xlabel("n of times")
plt.ylabel("time delta")
plt.show()

