# %%
from math import *
import decimal
def func1(n):
    return log2(n)
# %%
def func2(n):
    return log10(n)
#%%
import timeit
def time_check(func):
    start_time = timeit.default_timer() # 시작 시간 체크
    for n in range(2, 6000000):
        func(n)
    terminate_time = timeit.default_timer() # 종료 시간 체크
    print("%f초 걸렸습니다." % (terminate_time - start_time))

time_check(func1)
time_check(func2)


# %%
